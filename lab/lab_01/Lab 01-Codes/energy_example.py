 # Filepaths for RAPL power doman registers
CORE_DOMAIN="/sys/class/powercap/intel-rapl:0:0/energy_uj"
PSYS_DOMAIN="/sys/class/powercap/intel-rapl:1/energy_uj"

def read_energy_uj(file_path):
    try:
        with open(file_path, 'r') as file:
            energy_uj = file.read().strip()
        return int(energy_uj)
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except ValueError:
        print(f"Could not convert data to an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read the counters for each domain
initial_core_energy = read_energy_uj(CORE_DOMAIN)
initial_platform_energy = read_energy_uj(PSYS_DOMAIN)

# Your Code

final_core_energy = read_energy_uj(CORE_DOMAIN)       
final_platform_energy = read_energy_uj(PSYS_DOMAIN) 

core_energy_used = final_core_energy - initial_core_energy
if (core_energy_used < 0):
    print(f"Counter overflow core energy: {core_energy_used}")
else:
    # save the core energy used

platform_energy_used = final_platform_energy - initial_platform_energy      
if (platform_energy_used < 0):
    print(f"Counter overflow psys energy: {platform_energy_used}")
else:  
     # save the platform energy used
