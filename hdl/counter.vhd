library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity counter is
  generic (
    WIDTH : integer := 32);
  port (
    clk   : in  std_logic;
    rstn  : in  std_logic;
    ena   : in  std_logic;
    count : out std_logic_vector(WIDTH-1 downto 0));
end entity counter;

architecture rtl of counter is
  signal count_r : std_logic_vector(WIDTH-1 downto 0);
begin
  U0_PROC : process(clk, rstn)
  begin
    if rstn = '0' then
      count_r <= (others => '0');
    else
      if rising_edge(clk) then
        if ena = '1' then
          count_r <= std_logic_vector(unsigned(count_r) + 1);
        end if;
      end if;
    end if;
  end process;

  count <= count_r;
end architecture rtl;
