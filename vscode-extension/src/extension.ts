import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('NeuroCache extension is now active!');

    let disposable = vscode.commands.registerCommand('neurocache.completeCode', () => {
        vscode.window.showInformationMessage('NeuroCache: Complete Code command executed!');
        // Here you would add your actual completion logic or API call
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
