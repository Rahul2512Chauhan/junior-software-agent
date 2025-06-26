// hello.ts
function greet(name: string | null) {
    if (name === null) {
        console.log("Hello, there!"); // Handle null input
        return;
    }
    console.log(`Hello, ${name}`);
}

greet("world");
greet(null);
