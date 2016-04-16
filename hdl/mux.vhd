library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity mux is
  port (
    in0  : in  std_logic_vector(0 downto 0);
    in1  : in  std_logic_vector(0 downto 0);
    sel  : in  std_logic_vector(0 downto 0);
    out0 : out std_logic_vector(0 downto 0));
end entity mux;

architecture rtl of mux is
begin
  out0 <= in0 when (sel = "0") else in1;
end architecture rtl;
