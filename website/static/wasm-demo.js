let wasm;

async function loadWasm() {
    try {
        const module = await import('./pkg/rust_gpu.js');
        await module.default();
        wasm = module;
        console.log('WASM module loaded successfully');
        return true;
    } catch (error) {
        console.error('Failed to load WASM module:', error);
        return false;
    }
}

function runTensorDemo() {
    if (!wasm) {
        document.getElementById('tensor-result').innerHTML = '<p style="color: red;">WASM not loaded yet. Please wait...</p>';
        return;
    }
    
    try {
        const result = wasm.add_tensors();
        document.getElementById('tensor-result').innerHTML = `<pre>${result}</pre>`;
    } catch (error) {
        document.getElementById('tensor-result').innerHTML = `<p style="color: red;">Error: ${error}</p>`;
    }
}

function runMatrixDemo() {
    if (!wasm) {
        document.getElementById('matrix-result').innerHTML = '<p style="color: red;">WASM not loaded yet. Please wait...</p>';
        return;
    }
    
    try {
        const a = [1, 2, 3, 4];
        const b = [5, 6, 7, 8];
        const result = wasm.matrix_multiply(a, b, 2, 2);
        
        document.getElementById('matrix-result').innerHTML = `
            <div>
                <p>Matrix A: [[1, 2], [3, 4]]</p>
                <p>Matrix B: [[5, 6], [7, 8]]</p>
                <p>Result: [[${result[0]}, ${result[1]}], [${result[2]}, ${result[3]}]]</p>
            </div>
        `;
    } catch (error) {
        document.getElementById('matrix-result').innerHTML = `<p style="color: red;">Error: ${error}</p>`;
    }
}

window.addEventListener('load', async () => {
    const loaded = await loadWasm();
    if (loaded) {
        document.getElementById('wasm-status').innerHTML = '<span style="color: green;">✓ WASM loaded</span>';
    } else {
        document.getElementById('wasm-status').innerHTML = '<span style="color: red;">✗ WASM failed to load</span>';
    }
});