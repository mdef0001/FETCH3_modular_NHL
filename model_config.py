###############################################################################
# PHYSICAL CONSTANTS
###############################################################################
Rho = 1000  ##[kg m-3]
g = 9.8 # [m s-2]

###############################################################################
#INPUT DATA FILE PARAMETERS
###############################################################################

input_fname = "Derek_data_up.csv"

start_time = "2007-01-01 00:00:00" #begining of simulation
end_time = "2007-01-01 00:02:00" #end of simulation
#Full Simulation
# start_time = "2007-01-01 00:00:00" #begining of simulation
# end_time = "2007-06-09 00:00:00" #end of simulation

dt = 1800  #seconds - input data resolution
tmin = 0  #tmin [s]

###############################################################################
#RUN OPTIONS - printing
###############################################################################
# Printing slows down model run
# Options to turn printing off or specify print frequency
print_run_progress = True  # Turn on/off printing for progress of time steps calculated
print_freq = 50  # Interval of timesteps to print if print_run_progress = True (e.g. 1 will print every time step)

###############################################################################
#TRANSPIRATION OPTIONS - PENMAN-MONTEITH OR FETCH2 NHL
###############################################################################
transpiration_scheme = 0 # 0: PM transpiration; 1: NHL transpiration

###############################################################################
#NUMERICAL SOLUTION TIME AND SPACE CONSTANTS (dz and dt0)
###############################################################################
#The finite difference discretization constants
dt0 = 20  #model temporal resolution [s]
dz = 0.1  #model spatial resolution [m]

stop_tol = 0.0001  #stop tolerance of equation converging

#############################################################################
#MODEL PARAMETERS
#Values according to Verma et al., 2014
############################################################################

#CONFIGURING SOIL BOUNDARY CONDITIONS
#Here the user can choose the desired contition by setting the numbers as
#described below

#The configuration used follows Verma et al. 2014

#############################################################################

#Upper Boundary condition

#1 = no flux (Neuman)
#0 = infiltration


#Bottom Boundary condition

#2 = free drainage
#1 = no flux (Neuman)
#0 = constant potential (Dirichlet)

UpperBC=0
BottomBC=0

#SOIL SPATIAL DISCRETIZATION

Root_depth=3.2 #[m] depth of root column
Soil_depth=5   #[m]depth of soil column

####################################################################
#CONFIGURATION OF SOIL DUPLEX
#depths of layer/clay interface
#####################################################################

sand_d=5.0 #4.2----top soil #m
clay_d=4.2 #0------4.2 #m

#SOIL INITIAL CONDITIONS
#soil initial conditions as described in the paper [VERMA et al., 2014]
#the initial conditions were constant -6.09 m drom 0-3 metres (from soil bottom)
#from 3 meters, interpolation of -6.09 m to -0.402 m between 3-4.2 m
#from 4,2 m [sand layer] cte value of -0.402 m

cte_clay=3 #depth from 0-3m initial condition of clay [and SWC] is constant
H_init_soilbottom = -6.09
H_init_soilmid = -0.402
H_init_canopytop = -23.3

#SOIL PARAMETERS - USING VAN GENUCHTEN RELATIONSHIPS

#CLAY
alpha_1=0.8                        #soil hydraulic parameter [1/m]
theta_S1=0.55                      #saturated volumetric soil moisture content [-]
theta_R1=0.068                     #residual volumetric soil moisture content [-]
n_1=1.5                            #soil hydraulic parameter  [-]
m_1=1-(1/n_1)                      #soil hydraulic parameter  [-]
Ksat_1=1.94*10**(-7)               #saturated hydraulic conductivity  [m/s]

#SAND
alpha_2=14.5
theta_S2=0.47
theta_R2=0.045
n_2=2.4
m_2=1-(1/n_2)
Ksat_2=3.45*10**(-5)

#Soil stress parameters
theta_1_clay=0.08
theta_2_clay=0.12

theta_1_sand=0.05
theta_2_sand=0.09

#ROOT PARAMETERS
#diving by Rho*g since Richards equation is being solved in terms of \Phi (Pa)
Kr=(7.2*10**(-10))/(Rho*g) #soil-to-root radial conductance [m/sPa]
qz=9                                           #unitless - parameter for the root mass distribution - Verma et al., 2014
Ksax=(10**(-5))/(Rho*g)    #specific axial conductivity of roots  [ m/s]
Aind_r=1                                       #m2 root xylem/m2 ground]

#XYLEM PARAMETERS
kmax=(10**(-5))/(Rho*g)    #conductivity of xylem  [ m2/sPa]
ap=2*10**(-6)                                  #xylem cavitation parameter [Pa-1]
bp=-1.5*10**(6)                                #xylem cavitation parameter [Pa]
Aind_x=8.62*10**(-4)                           #m2 xylem/m2 ground]
Phi_0=5.74*10**8                               #From bohrer et al 2005
p=20                                           #From bohrer et al 2005
sat_xylem=0.573                                #From bohrer et al 2005

#TREE PARAMETERS
Hspec=22                      #Height average of trees [m]
LAI=1.5                       #[-] Leaf area index
Abasal=8.62*10**(-4)          #[m2basal/m2-ground] xylem cross-sectional area and site surface ratio

#######################################################################
#LEAF AREA DENSITY FORMULATION (LAD) [1/m]
#######################################################################
LAI=1.5                #[-] Leaf area index

#parameters if using penman-monteith transpiration scheme, based on Lalic et al 2014
#if using NHL transpiration scheme, LAD is calculated in NHL module
L_m=0.4  #maximum value of LAD a canopy layer
z_m=11   #height in which L_m is found [m]

###########################################################################
#PENMAN-MONTEITH EQUATION PARAMETERS
###########################################################################
#W m^-2 is the same as J s^-1 m^-2
#1J= 1 kg m2/s2
#therefore 1W/m2 = kg/s3

gb=2*10**(-2)          #m/s Leaf boundary layer conductance
Cp=1200                # J/m3 K Heat capacity of air
ga=2*10**(-2)          #m/s Aerodynamic conductance
lamb=2.51*10**9        #J/m3 latent heat of vaporization
gama=66.7              #Pa/K psychrometric constant

#########################################################################3
#JARVIS PARAMETERS
###########################################################################

gsmax=10*10**(-3)      #m/s Maximum leaf stomatal conductance
kr=5*10**(-3)         #m2/W Jarvis radiation parameter
kt=1.6*10**(-3)       #K-2  Jarvis temperature parameter
Topt=289.15           #K   Jarvis temperature parameter (optimum temperature)
kd=1.1*10**(-3)       #Pa-1 Jarvis vapor pressure deficit temperature
hx50=-1274000         #Pa  Jarvis leaf water potential parameter
nl=2                   #[-] Jarvis leaf water potential parameter
Emax=1*10**(-9)        #m/s maximum nightime transpiration
