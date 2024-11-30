#!/usr/bin/env node

class Client {
    constructor(socketPath) {
        this.client = require('node:net').createConnection(socketPath);
        this.client.on('data', this.handleData.bind(this));
        this.client.on('end', this.handleEnd.bind(this));
        this.client.on('error', this.handleError.bind(this));
    }

    sendRequest(request) {
        this.client.write(JSON.stringify(request));
    }

    getUserInput() {
        const readline = require('node:readline').createInterface({
            input: process.stdin,
            output: process.stdout
        });

        readline.question('\nEnter function name followed by parameters, separated by spaces: ', (input) => {
            const [method, ...params] = input.split(' ');
            this.sendRequest({ method, params });
            readline.close();
        });
    }

    handleData(data) {
        const response = JSON.parse(data);

        if('result' in response) {
            this.handleResult(response);
        }
        else if('error' in response) {
            this.handleError(response.error);
        }
        else {
            this.handleMethodInfo(response);
        }
        this.getUserInput();
    }

    handleMethodInfo(data) {
        console.log('-----------------------------------------------');
        for(const [funcName, funcDetails] of Object.entries(data)) {
            console.log(`\nFunction: ${funcName}`);
            console.log(`Description: ${funcDetails.description}`);
            console.log(`Parameters: ${funcDetails.params}`);
            console.log(`Return: ${funcDetails.return}`);
        }
        console.log('-----------------------------------------------\n');
    }

    handleResult(data) {
        console.log('------ Response from the server ------')
        for(const [key, value] of Object.entries(data)) {
            console.log(`${key}: ${value}`);
        }
    }

    handleError(error) {
        console.log('------ Response from the server ------')
        console.error('error:', error);
    }

    handleEnd() {
        console.log('\nServer disconnected.');
    }
}

const client = new Client('/tmp/echo.sock');
