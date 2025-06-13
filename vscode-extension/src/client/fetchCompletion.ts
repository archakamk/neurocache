interface CompletionResponse {
    completion: string;
  }
  
  export async function fetchCompletion(prompt: string): Promise<string> {
    const response = await fetch('http://localhost:8000/complete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
  
    if (!response.ok) {
      throw new Error(`Server error: ${response.statusText}`);
    }
  
    // Tell TypeScript what the data looks like:
    const data: CompletionResponse = await response.json();
  
    return data.completion;
  }
  