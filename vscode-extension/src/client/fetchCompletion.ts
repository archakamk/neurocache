import fetch from 'node-fetch';

export async function fetchCompletion(prompt: string): Promise<string> {
    const response = await fetch("http://localhost:8000/complete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    return data.completion;
}
