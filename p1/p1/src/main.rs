use std::{
    env,
    fs::File,
    io::{prelude::*, Error,ErrorKind, BufReader},
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

fn fuel_requirements(module_masses: Vec<i32>)  -> i32 {
    
    let mut total: i32 = 0;
    for mass in module_masses {
        total += mass/3 - 2;    
    }

   total
}


fn main() {
    let args: Vec<String> = env::args().collect();
    let ship_components = &args[1];
    
    let modules = modules_from_file(ship_components);

    for module in modules {
        println!("{:?}", module);
        let total_mass = fuel_requirements(module);
        println!("[+] Total mass : {}", total_mass);
    }

    //
} 