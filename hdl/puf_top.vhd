library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity puf_top is
  port (
    clk           : in  std_logic;
    rstn          : in  std_logic;
    -- Avalon Slave Signals
    avs_address   : in  std_logic_vector(31 downto 0);
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
      challenge_input : in  std_logic_vector(INPUT_WIDTH-1 downto 0);
      response_output : out std_logic_vector(OUTPUT_WIDTH-1 downto 0));
  end component puf;
  signal control_reg : std_logic_vector(31 downto 0);
  signal input_reg   : std_logic_vector(1023 downto 0);
  signal output_reg  : std_logic_vector(31 downto 0);
  signal puf_rstn    : std_logic;
  signal puf_ena     : std_logic;
begin
  U0_PUF : puf
    generic map (
      INPUT_WIDTH    => 1024,
      OUTPUT_WIDTH   => 32,
      RING_OSC_DEPTH => 20)
    port map (
      clk             => clk,
      rstn            => puf_rstn,
      ena             => puf_ena,
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
            when x"00000000" =>
              avs_readdata <= control_reg;
            when x"00000001" =>
              avs_readdata <= output_reg;
            when others =>
              avs_readdata <= (others => 'X');
          end case;
        end if;
      end if;x
    end if;
  end process;

  U2_WRITE_PROC : process(clk, rstn)
  begin
    if rising_edge(clk) then
      if avs_write = '1' then
        case avs_address is
          when x"00000000" =>
            control_reg <= avs_writedata;
          when x"00000001" =>
            input_reg(1023 downto 992) <= avs_writedata;
          when x"00000002" =>
            input_reg(991 downto 960) <= avs_writedata;
          when x"00000003" =>
            input_reg(959 downto 928) <= avs_writedata;
          when x"00000004" =>
            input_reg(927 downto 896) <= avs_writedata;
          when x"00000005" =>
            input_reg(895 downto 864) <= avs_writedata;
          when x"00000006" =>
            input_reg(863 downto 832) <= avs_writedata;
          when x"00000007" =>
            input_reg(831 downto 800) <= avs_writedata;
          when x"00000008" =>
            input_reg(799 downto 768) <= avs_writedata;
          when x"00000009" =>
            input_reg(767 downto 736) <= avs_writedata;
          when x"0000000A" =>
            input_reg(735 downto 704) <= avs_writedata;
          when x"0000000B" =>
            input_reg(703 downto 672) <= avs_writedata;
          when x"0000000C" =>
            input_reg(671 downto 640) <= avs_writedata;
          when x"0000000D" =>
            input_reg(639 downto 608) <= avs_writedata;
          when x"0000000E" =>
            input_reg(607 downto 576) <= avs_writedata;
          when x"0000000F" =>
            input_reg(575 downto 544) <= avs_writedata;
          when x"00000010" =>
            input_reg(543 downto 512) <= avs_writedata;
          when x"00000011" =>
            input_reg(511 downto 480) <= avs_writedata;
          when x"00000012" =>
            input_reg(479 downto 448) <= avs_writedata;
          when x"00000013" =>
            input_reg(447 downto 416) <= avs_writedata;
          when x"00000014" =>
            input_reg(415 downto 384) <= avs_writedata;
          when x"00000015" =>
            input_reg(383 downto 352) <= avs_writedata;
          when x"00000016" =>
            input_reg(351 downto 320) <= avs_writedata;
          when x"00000017" =>
            input_reg(319 downto 288) <= avs_writedata;
          when x"00000018" =>
            input_reg(287 downto 256) <= avs_writedata;
          when x"00000019" =>
            input_reg(255 downto 224) <= avs_writedata;
          when x"0000001A" =>
            input_reg(223 downto 192) <= avs_writedata;
          when x"0000001B" =>
            input_reg(191 downto 160) <= avs_writedata;
          when x"0000001C" =>
            input_reg(159 downto 128) <= avs_writedata;
          when x"0000001D" =>
            input_reg(127 downto 96) <= avs_writedata;
          when x"0000001E" =>
            input_reg(95 downto 64) <= avs_writedata;
          when x"0000001F" =>
            input_reg(63 downto 32) <= avs_writedata;
          when x"00000020" =>
            input_reg(31 downto 0) <= avs_writedata;
        end case;
      end if;
    end if;
  end process;

  --Assign the signal
  puf_rstn <= not control_reg(31);
  puf_ena  <= control_reg(0);

end architecture rtl;
