import * as vscode from 'vscode';
import { fetchCompletion } from './client/fetchCompletion';

export function activate(context: vscode.ExtensionContext) {
  console.log('NeuroCache extension is active');

  let disposable = vscode.commands.registerCommand('neurocache.completeCode', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showWarningMessage('Open a file to use NeuroCache!');
      return;
    }

    const document = editor.document;
    const position = editor.selection.active;
    const lineText = document.lineAt(position.line).text;

    vscode.window.setStatusBarMessage('NeuroCache is thinking...', 3000);

    try {
      const completion = await fetchCompletion(lineText);

      await editor.edit(editBuilder => {
        editBuilder.insert(position, completion);
      });

      vscode.window.setStatusBarMessage('NeuroCache completion inserted!', 3000);

    } catch (err: any) {
      vscode.window.showErrorMessage('Error fetching completion: ' + err.message);
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
