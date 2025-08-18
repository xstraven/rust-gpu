#![recursion_limit = "256"]

use burn::prelude::*;
use burn::backend::Wgpu;

fn main() {
    let device = Default::default();
    
    let tensor1 = Tensor::<Wgpu, 2>::from_data([[1.0, 2.0], [3.0, 4.0]], &device);
    let tensor2 = Tensor::<Wgpu, 2>::from_data([[5.0, 6.0], [7.0, 8.0]], &device);
    
    let result = tensor1 + tensor2;
    
    println!("Hello from Rust GPU with Burn!");
    println!("Tensor addition result: {:?}", result.to_data());
}