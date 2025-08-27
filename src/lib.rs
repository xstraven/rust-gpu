use wasm_bindgen::prelude::*;
use burn::prelude::*;

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
    
    #[wasm_bindgen(js_namespace = console)]
    fn log(s: &str);
}

macro_rules! console_log {
    ($($t:tt)*) => (log(&format_args!($($t)*).to_string()))
}

#[wasm_bindgen]
pub fn greet(name: &str) {
    alert(&format!("Hello, {}!", name));
}

#[wasm_bindgen]
pub fn add_tensors() -> String {
    console_log!("Starting tensor operations...");
    
    let device = Default::default();
    
    let tensor1 = Tensor::<burn::backend::Candle, 2>::from_data([[1.0, 2.0], [3.0, 4.0]], &device);
    let tensor2 = Tensor::<burn::backend::Candle, 2>::from_data([[5.0, 6.0], [7.0, 8.0]], &device);
    
    let result = tensor1 + tensor2;
    
    let result_data = result.to_data();
    format!("Tensor addition result: {:?}", result_data)
}

#[wasm_bindgen]
pub fn matrix_multiply(a: &[f64], b: &[f64], rows: usize, cols: usize) -> Vec<f64> {
    console_log!("Performing matrix multiplication...");
    
    let mut result = vec![0.0; rows * cols];
    
    for i in 0..rows {
        for j in 0..cols {
            for k in 0..cols {
                result[i * cols + j] += a[i * cols + k] * b[k * cols + j];
            }
        }
    }
    
    result
}