library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity comparator is
  port (
    val_a    : in  std_logic;
    val_b    : in  std_logic;
    solution : out std_logic);
end entity comparator;

architecture rtl of comparator is
begin
  solution <= '1' when (unsigned(val_a) > unsigned(val_b)) else '0';
end architecture rtl;
