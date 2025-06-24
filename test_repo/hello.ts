// hello.ts
function greet(name: string | null) {
    console.log(`Hello, ${name ?? "world"}`);
}

greet("world");
greet(null);
