// hello.ts
function greet(name: string | null) {
    console.log(`Hello, ${name ?? "Guest"}`);
}

greet("world");
greet(null);