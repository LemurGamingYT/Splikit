# Splikit
 Simple, fast programming language written in Python that compiles to C++.

---

# Features
- **Speed**: Splikit is compiled to C++, which is one of the fastest languages. While optimizations on the C++ code can definitely be done, it is still a fast language.
- **Static typing**: While Splikit is statically typed because of the compilation to C++, Splikit does have type inference for variables. However, you do need to explicitly say what type a function returns and it's parameters.
- **Simplicity**: Splikit's syntax is very simple, almost like a bridge between Python and C++.

---

# Running the language

1. Clone this repository
    - If you have the `git` command line tool, you can use that to install the repository using: `git clone https://github.com/LemurGamingYT/Splikit.git`
    - If you don't have `git`, then you can install the repository as a .zip by clicking the drop down menu: 'Code' and then 'Download ZIP'
2. Install Python
    - You should install the latest version of Python
    - During the setup, add Python to PATH and install `pip` and run the command: `pip install -r requirements.txt` in the directory you have downloaded this repository.
3. Install a C++ compiler
    - MinGW (g++): https://sourceforge.net/projects/mingw/files/latest/download
    - LLVM (clang++): https://github.com/llvm/llvm-project/releases
        - You can also download LLVM using Chocolatey: `choco install llvm`
4. Run the compiler
    - Use the command: `python main.py [.spk file]` to compile a .spk file to C++ and run it.

---

# Ideas

- **C++ interoperability**: Splikit is compiled to C++ and therefore, it should be possible to interop with C++ libraries and functions. This could be done by converting C++ libraries into Splikit-compatible ones. *(Expect this to come **way** later because this could probably take months to properly implement)*
```
// First, the compiler will compile the symbols in the header into a Splikit-compatible one.
// Next, the compiler will #include the header in the generated C++ code from the .spk file.
extern use "some_ui_library.hpp"

// Use a function from it
window = create_window("Example usage title")
```
- **Dictionaries/Maps**: Maps are supported in C++, meaning it's possible for Splikit to have them.
```
// Create a new dictionary
dictionary = Dict[string: int] {
    "a": 1,
    "b": 2,
    "c": 3
}

print(dictionary)

// Use dictionary functions
print(dictionary.get("a")) // 1
print(dictionary.from_value(3)) // "c"
```
- **Function expressions**: Lambda function equivalent.
```
print((int x) => { return x - 20 }(20)) // 0
```
- **Reference parameters**: Pass parameters by reference, meaning anything that it changes with the parameter in the function will change outside the function too.
```
// 'ref' indicates it will be passed by reference
func test(ref int x) {
    x = x + 1000
}

// Define the 'x' variable
x = 50

// Call the function, 'x' is passed by reference
test(x)
print(x) // 1050, 'x' was changed in the function
```
- **Structs**: Custom types in Splikit. Supported in C++ too meaning it can almost be directly translated into C++.
```
// Create a new struct
struct Vector3 {
    float x
    float y
    float z
}

// Make a method on the Vector3 struct
func Vector3.repr(Vector3 vec) { // Create a string representation of the struct
    return "Vector3(x=" + to_string(vec.x) + ", y=" + to_string(vec.y) + ", z=" + to_string(vec.z) + ")"
}

// Create a new property that is static
// Properties do not need to be called, methods do
// If the property or method is static (like this one), then no parameters are needed.
// Properties or methods that are not static, take in the instance of the struct.
static property Vector3.zero() -> Vector3 {
    return Vector3{0, 0, 0}
}

// Create a new Vector3 object
vec_zero = Vector3.zero
vec = Vector3{70, 0, 120}
print(vec) // 'Vector3.repr' is called
```
- **Compile time expressions**: Expressions or functions evaluated at compile time instead of run time. This could make use of C++'s constexpr keyword, however this would mean that the feature would be limited to ints and floats.
```
comptime {
    func factorial(int n) -> int {
        if n == 0 || n == 1 {
            return 1
        } else {
            return n * factorial(n - 1)
        }
    }
}

print(factorial(5)) // This is evaluated at compile time and is replaced with the value of 120 in the generated assembly code.
```
