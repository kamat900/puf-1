library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity puf_top is
  generic (
    WIDTH          : integer := 32;
    RING_OSC_DEPTH : integer := 20);
  port (
    clk             : in  std_logic;
    rstn            : in  std_logic;
    ena             : in  std_logic;
    challenge_input : in  std_logic_vector(WIDTH-1 downto 0);
    response_output : out std_logic_vector(WIDTH-1 downto 0));
end entity puf_top;

architecture rtl of puf_top is
  component ring_oscillator is
    generic (
      CHAIN_WIDTH : positive);
    port (
      rstn   : in  std_logic;
      output : out std_logic);
  end component ring_oscillator;
  component comparator is
    port (
      val_a    : in  std_logic;
      val_b    : in  std_logic;
      solution : out std_logic);
  end component comparator;
begin

end architecture rtl;
