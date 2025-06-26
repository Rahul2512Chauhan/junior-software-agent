// hello.ts
function greet(name: string | null) {
    // Check if name is null before using it.  If null, provide a default greeting.
    const nameToUse = name ?? "Guest"; 
    console.log(`Hello, ${nameToUse}`);
}

greet("world");
greet(null);
