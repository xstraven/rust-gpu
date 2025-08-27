from fasthtml.common import *
import os

app, rt = fast_app(
    live=True,
    hdrs=[
        Style("""
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 1200px; margin: 0 auto; padding: 2rem; }
            .hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 3rem; border-radius: 12px; margin-bottom: 2rem; }
            .card { border: 1px solid #e5e5e5; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; }
            .code-block { background: #f8f9fa; padding: 1rem; border-radius: 6px; overflow-x: auto; }
            pre { margin: 0; }
            nav { margin-bottom: 2rem; }
            nav a { margin-right: 1rem; text-decoration: none; color: #667eea; }
            nav a:hover { text-decoration: underline; }
            .demo-section { border-left: 4px solid #667eea; padding-left: 1rem; margin: 2rem 0; }
        """)
    ]
)

def nav_bar():
    return Nav(
        A("Home", href="/"),
        A("Tensor Operations", href="/tensors"),
        A("WASM Demos", href="/wasm"),
        A("Source Code", href="/source")
    )

@rt("/")
def home():
    return Title("Rust GPU Experiments"), Main(
        nav_bar(),
        Div(cls="hero")(
            H1("Rust GPU Experiments"),
            P("Exploring GPU workloads with Rust, burn.dev, and WebAssembly"),
            P("This site showcases experiments with GPU-accelerated computing using modern Rust tooling.")
        ),
        Div(cls="card")(
            H2("🔥 burn.dev"),
            P("Deep learning framework for Rust with GPU acceleration support"),
            P("Current experiments include tensor operations and neural network primitives.")
        ),
        Div(cls="card")(
            H2("🕸️ WebAssembly"),
            P("Running Rust computations directly in the browser"),
            P("Compile GPU workloads to WASM for interactive web demonstrations.")
        ),
        Div(cls="card")(
            H2("⚡ GPU Computing"),
            P("Leveraging WebGPU and compute shaders for parallel processing"),
            P("Compare CPU vs GPU performance for various computational tasks.")
        )
    )

@rt("/tensors")
def tensors():
    rust_code = """use burn::prelude::*;
use burn::backend::Wgpu;

fn main() {
    let device = Default::default();
    
    let tensor1 = Tensor::<Wgpu, 2>::from_data([[1.0, 2.0], [3.0, 4.0]], &device);
    let tensor2 = Tensor::<Wgpu, 2>::from_data([[5.0, 6.0], [7.0, 8.0]], &device);
    
    let result = tensor1 + tensor2;
    
    println!("Tensor addition result: {:?}", result.to_data());
}"""
    
    return Title("Tensor Operations"), Main(
        nav_bar(),
        H1("Tensor Operations with burn.dev"),
        
        Div(cls="demo-section")(
            H2("Basic Tensor Addition"),
            P("This example demonstrates basic tensor operations using burn.dev with GPU acceleration:"),
            Div(cls="code-block")(
                Pre(Code(rust_code))
            ),
            P("Result: [[6.0, 8.0], [10.0, 12.0]]")
        ),
        
        Div(cls="card")(
            H3("Performance Notes"),
            Ul(
                Li("GPU operations are asynchronous and batched for efficiency"),
                Li("Small tensors may be faster on CPU due to overhead"),
                Li("GPU acceleration shines with larger tensor operations")
            )
        )
    )

@rt("/wasm")
def wasm():
    return Title("WASM Demos"), Main(
        nav_bar(),
        H1("WebAssembly Demonstrations"),
        
        Div(id="wasm-status")(
            "Loading WASM module..."
        ),
        
        Div(cls="demo-section")(
            H2("Tensor Operations"),
            P("Run burn.dev tensor operations compiled to WebAssembly:"),
            Button("Run Tensor Demo", onclick="runTensorDemo()", style="padding: 0.5rem 1rem; margin: 0.5rem 0;"),
            Div(id="tensor-result", style="margin-top: 1rem; padding: 1rem; background: #f8f9fa; border-radius: 4px;")
        ),
        
        Div(cls="demo-section")(
            H2("Matrix Multiplication"),
            P("Basic matrix multiplication implemented in Rust and compiled to WASM:"),
            Button("Run Matrix Demo", onclick="runMatrixDemo()", style="padding: 0.5rem 1rem; margin: 0.5rem 0;"),
            Div(id="matrix-result", style="margin-top: 1rem; padding: 1rem; background: #f8f9fa; border-radius: 4px;")
        ),
        
        Div(cls="card")(
            H3("Build Instructions"),
            P("To build the WASM module:"),
            Div(cls="code-block")(
                Pre(Code("cd website && ./build_wasm.sh"))
            ),
            P("This will generate the WASM files in static/pkg/")
        ),
        
        Script(src="/static/wasm-demo.js", type="module")
    )

@rt("/source")
def source():
    return Title("Source Code"), Main(
        nav_bar(),
        H1("Source Code Examples"),
        
        Div(cls="demo-section")(
            H2("Repository Structure"),
            Div(cls="code-block")(
                Pre(Code("""rust-gpu/
├── src/main.rs          # Main Rust application
├── Cargo.toml           # Rust dependencies
├── website/             # FastHTML website
│   ├── app.py          # Web application
│   └── pyproject.toml  # Python dependencies
└── README.md           # Project overview"""))
            )
        ),
        
        Div(cls="card")(
            H3("Key Dependencies"),
            Ul(
                Li("burn = { version = \"0.18.0\", features = [\"wgpu\"] }"),
                Li("fasthtml >= 0.6.9"),
                Li("uvicorn for serving the web application")
            )
        )
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)