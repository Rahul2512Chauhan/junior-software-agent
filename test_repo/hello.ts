// hello.ts
function greet(name: string | null | undefined) {
    // Handle null or undefined input
    const nameToGreet = name ?? "Guest"; 
    console.log(`Hello, ${nameToGreet}`);
}

greet("world");
greet(null);
greet(undefined);