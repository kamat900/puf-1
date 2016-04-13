library IEEE;
use IEEE.std_logic_1164.all ;
use IEEE.numeric_std.all ;

entity ring_oscillator is
  generic (
    CHAIN_WIDTH : positive := 50 -- must be an even number
  ) ;
  port (
    rstn   : in  std_logic;
    output : out std_logic
  );
end entity ring_oscillator;

architecture rtl of ring_oscillator is
  signal chain    : unsigned(CHAIN_WIDTH downto 0);
  signal s_output : std_logic;
  attribute syn_keep : boolean;
  attribute syn_keep of chain : signal is true;
begin
  U0_GEN_OSC_CHAIN: for i in 1 to CHAIN_WIDTH
  generate
    chain(i) <= chain(i - 1) ;
  end generate;
  chain(0) <= not chain(CHAIN_WIDTH) or (not rst_n) ;

  U1_PROC_TFF: process (rst_n, chain(0))
  begin
    if rst_n = '0' then
      s_output <= '0';
    else
      if rising_edge(chain(0)) then
        s_output <= not s_output;
      end if;
    end if;
  end process;
  output <= s_output;
end architecture rtl;
