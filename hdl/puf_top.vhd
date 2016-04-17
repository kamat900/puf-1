library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity puf_top is
  port (
    clk           : in  std_logic;
    rstn          : in  std_logic;
    -- Avalon Slave Signals
    avs_address   : in  std_logic_vector(11 downto 0);
    avs_write     : in  std_logic;
    avs_writedata : in  std_logic_vector(31 downto 0);
    avs_read      : in  std_logic;
    avs_readdata  : out std_logic_vector(31 downto 0));
end entity puf_top;

architecture rtl of puf_top is
  component puf is
    generic (
      INPUT_WIDTH    : integer;
      OUTPUT_WIDTH   : integer;
      RING_OSC_DEPTH : integer);
    port (
      clk             : in  std_logic;
      rstn            : in  std_logic;
      ena             : in  std_logic;
      done            : out std_logic;
      challenge_input : in  std_logic_vector(INPUT_WIDTH-1 downto 0);
      response_output : out std_logic_vector(OUTPUT_WIDTH-1 downto 0));
  end component puf;
  signal control_reg : std_logic_vector(31 downto 0);
  signal input_reg   : std_logic_vector(127 downto 0);
  signal output_reg  : std_logic_vector(31 downto 0);
  signal puf_rstn    : std_logic;
  signal puf_ena     : std_logic;
  signal puf_done    : std_logic;
begin
  U0_PUF : puf
    generic map (
      INPUT_WIDTH    => 128,
      OUTPUT_WIDTH   => 32,
      RING_OSC_DEPTH => 20)
    port map (
      clk             => clk,
      rstn            => puf_rstn,
      ena             => puf_ena,
      done            => puf_done,
      challenge_input => input_reg,
      response_output => output_reg);

  U1_READ_PROC : process(clk, rstn)
  begin
    if rstn = '0' then
      avs_readdata <= (others => '0');
    else
      if rising_edge(clk) then
        if avs_read = '1' then
          case avs_address is
            when x"000" =>
              avs_readdata <= control_reg;
            when x"001" =>
              avs_readdata <= output_reg(31 downto 0);
            when others =>
              avs_readdata <= (others => 'X');
          end case;
        end if;
      end if;
    end if;
  end process;

  U2_WRITE_PROC : process(clk, rstn)
  begin
    if rising_edge(clk) then
      if avs_write = '1' then
        case avs_address is
          when x"000" =>
            control_reg(31 downto 2) <= avs_writedata(31 downto 2);
            control_reg(0)           <= avs_writedata(0);
          when x"001" =>
            input_reg(127 downto 96) <= avs_writedata;
          when x"002" =>
            input_reg(95 downto 64) <= avs_writedata;
          when x"003" =>
            input_reg(63 downto 32) <= avs_writedata;
          when x"004" =>
            input_reg(31 downto 0) <= avs_writedata;
          when others =>
        end case;
      end if;
    end if;
  end process;

  --Assign the signal
  puf_rstn       <= not control_reg(31);
  puf_ena        <= control_reg(0);
  control_reg(1) <= puf_done;
end architecture rtl;
