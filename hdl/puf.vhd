library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity puf is
  generic (
    INPUT_WIDTH    : integer := 1024;
    PUTPUT_WIDTH   : integer := 32;
    RING_OSC_DEPTH : integer := 20);
  port (
    clk             : in  std_logic;
    rstn            : in  std_logic;
    ena             : in  std_logic;
    challenge_input : in  std_logic_vector(INPUT_WIDTH-1 downto 0);
    response_output : out std_logic_vector(OUTPUT_WIDTH-1 downto 0));
end entity puf;

architecture rtl of puf is
  constant OSC_NUM        : integer := 1024;
  constant COUNTER_NUM    : integer := 1024;
  constant COMPARATOR_NUM : integer := 512;
  constant MUX_LVL_1_NUM  : integer := 512;
  constant MUX_LVL_2_NUM  : integer := 256;
  constant MUX_LVL_3_NUM  : integer := 128;
  constant MUX_LVL_4_NUM  : integer := 64;
  constant MUX_LVL_5_NUM  : integer := 32;
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
  component counter is
    generic (
      WIDTH : integer);
    port (
      clk   : in  std_logic;
      rstn  : in  std_logic;
      ena   : in  std_logic;
      count : out std_logic_vector(WIDTH-1 downto 0));
  end component counter;
  component mux is
    port (
      in0  : in  std_logic;
      in1  : in  std_logic;
      sel  : in  std_logic;
      out0 : out std_logic);
  end component mux;
  signal osc_output    : std_logic_vector(OSC_NUM-1 downto 0);
  signal count         : std_logic_vector(COUNTER_NUM-1 downto 0);
  signal solution      : std_logic_vector(COMPARATOR_NUM-1 downto 0);
  signal mux_lvl_1_out : std_logic_vector(MUX_LVL_1_NUM-1 downto 0);
  signal mux_lvl_2_out : std_logic_vector(MUX_LVL_2_NUM-1 downto 0);
  signal mux_lvl_3_out : std_logic_vector(MUX_LVL_3_NUM-1 downto 0);
  signal mux_lvl_4_out : std_logic_vector(MUX_LVL_4_NUM-1 downto 0);
begin
  U0_GEN_RING_OSC : for i in 0 to OSC_NUM
  generate
    U0_OSC : ring_oscillator
      generic map (
        CHAIN_WIDTH => CHAIN_WIDTH)
      port map (
        rstn   => rstn,
        output => osc_output(i));
  end generate;

  U1_GEN_COUNTER : for i in 0 to COUNTER_NUM
  generate
    U1_COUNTER : counter
      generic map (
        WIDTH => WIDTH)
      port map (
        clk   => osc_output(i),
        rstn  => rstn,
        ena   => ena,
        count => count(i));
  end generate;

  U2_GEN_COMPARATOR : for i in 0 to COMPARATOR_NUM
  generate
    U2_COMPARATOR : comparator
      port map (
        val_a    => count(i*2),
        val_b    => count(i*2+1),
        solution => solution(i));
  end generate;

  U3_GEN_MUX_LVL_1 : for i in 0 to MUX_LVL_1_NUM
  generate
    U3_MUX_LVL_1 : mux
      port map (
        in0  => solution(i*2),
        in1  => solution(i*2+1),
        sel  => challenge_input(i),
        out0 => mux_lvl_1_out(i));
  end generate;

  U4_GEN_MUX_LVL_2 : for i in 0 to MUX_LVL_2_NUM
  generate
    U4_MUX_LVL_2 : mux
      port map (
        in0  => mux_lvl_1_out(i*2),
        in1  => mux_lvl_1_out(i*2+1),
        sel  => challenge_input(512+i),
        out0 => mux_lvl_2_out(i));
  end generate;

  U5_GEN_MUX_LVL_3 : for i in 0 to MUX_LVL_3_NUM
  generate
    U5_MUX_LVL_3 : mux
      port map (
        in0  => mux_lvl_2_out(i*2),
        in1  => mux_lvl_2_out(i*2+1),
        sel  => challenge_input(512+256+i),
        out0 => mux_lvl_3_out(i));
  end generate;

  U6_GEN_MUX_LVL_4 : for i in 0 to MUX_LVL_4_NUM
  generate
    U6_MUX_LVL_4 : mux
      port map (
        in0  => mux_lvl_3_out(i*2),
        in1  => mux_lvl_3_out(i*2+1),
        sel  => challenge_input(512+256+128+i),
        out0 => mux_lvl_4_out(i));
  end generate;

  U7_GEN_MUX_LVL_5 : for i in 0 to MUX_LVL_5_NUM
  generate
    U7_MUX_LVL_5 : mux
      port map (
        in0  => mux_lvl_4_out(i*2),
        in1  => mux_lvl_4_out(i*2+1),
        sel  => challenge_input(512+256+128+64+i),
        out0 => response_output(i));
  end generate;
end architecture rtl;
