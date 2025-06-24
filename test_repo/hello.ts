// hello.ts
function greet(name: string | null) {
    // Check if name is null before using it
    if (name === null) {
        console.log("Hello, there!"); // Handle null input
    } else {
        console.log(`Hello, ${name}`);
    }
}

greet("world");
greet(null);
