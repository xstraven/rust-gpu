#![recursion_limit = "256"]
mod data;
mod model;
mod training;

use crate::model::ModelConfig;
use crate::training::TrainingConfig;
use burn::backend::Wgpu;

use burn::{backend::Autodiff, optim::AdamConfig};

fn main() {
    type MyBackend = Wgpu<f32, i32>;
    type MyAutodiffBackend = Autodiff<MyBackend>;

    let device = burn::backend::wgpu::WgpuDevice::default();
    let artifact_dir = "/tmp/guide";
    crate::training::train::<MyAutodiffBackend>(
        artifact_dir,
        TrainingConfig::new(ModelConfig::new(10, 512), AdamConfig::new()),
        device.clone(),
    );
}
