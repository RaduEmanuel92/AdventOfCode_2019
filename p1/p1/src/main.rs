use std::{
    env,
    fs::File,
    io::{prelude::*, Error, ErrorKind, BufReader},
    path::Path
};


fn modules_from_file(filename: impl AsRef<Path>) -> Result<Vec<i32>, Error>  {
    let input_file = File::open(filename).expect("[-] Error: could not read file.");
    let reader = BufReader::new(input_file);
    let mut module_masses = Vec::new();
    
    for line in reader.lines() {
        module_masses.push(line?
            .trim().parse::<i32>()
            .map_err(|e| Error::new(ErrorKind::InvalidData, e))?);
    }
   
    Ok(module_masses) 
}

fn compute_mass(mass: i32) -> i32 {
    let fin_mass: i32 = mass/3 - 2;
    
    fin_mass
}

fn fuel_partial_requirements(module_masses: &Vec<i32>)  -> i32 {
    let mut total: i32 = 0;

    for mass in module_masses {
        total += compute_mass(*mass);    
    }

   total
}

fn fuel_final_requirements(module_masses: &Vec<i32>)  -> i32 {
    let mut total:   i32 = 0;
    let mut partial: i32 = 0;

    for mass in module_masses {
        partial = compute_mass(*mass);
        while partial > 0 {
            total += partial;
            partial = compute_mass(partial);
        }
    }

   total
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let ship_components = &args[1];
    let modules = modules_from_file(ship_components);

    for module in modules {
        println!("[+] Parsing modules...");
        println!("[+] 1. Partial quantity of fuel needed : {}", fuel_partial_requirements(&module));
        println!("[+] 2. Total quantity of fuel needed : {}", fuel_final_requirements(&module));
    }  
} 