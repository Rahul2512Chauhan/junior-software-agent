// hello.ts
function greet(name: string | null) {
    // Check if name is null or undefined before using it
    if (name === null || name === undefined) {
        console.log("Hello, there!"); // Handle null or undefined input
    } else {
        console.log(`Hello, ${name}`);
    }
}

greet("world");
greet(null);