#pragma once


#include <filesystem>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>


#define VERSION "0.0.1"

#define PI 3.14159265358979323846
#define ONE_BILLION 1000000000
#define ONE_MILLION 1000000
#define ONE_THOUSAND 1000
#define MAX_INT 2147483647
#define MIN_INT -2147483648


#if defined(_WIN32) || defined(_WIN64)
    #define OS_WINDOWS
    #ifndef NO_WIN32_LEAN_AND_MEAN
        #define NO_WIN32_LEAN_AND_MEAN
    #endif

    #ifndef NOMINMAX
        #define NOMINMAX
    #endif

    #include <Windows.h>
#elif defined(__unix__)
    #define OS_UNIX
    #include <unistd.h>
#endif


using nil = std::nullptr_t;
using std::string;


struct MathType{};
#define Math MathType{}

struct SystemType{};
#define System SystemType{}

struct SplikitType{};
#define Splikit SplikitType{}

// struct IntegerType{};
// #define Integer IntegerType{}


inline string type(int _) { return "int"; }
inline string type(float _) { return "float"; }
inline string type(string _) { return "string"; }
inline string type(bool _) { return "bool"; }
inline string type(nil _) { return "nil"; }
inline string type(MathType _) { return "Math"; }
inline string type(SystemType _) { return "System"; }
inline string type(SplikitType _) { return "Splikit"; }
// inline string type(IntegerType _) { return "IntegerClass"; }

inline string repr(int x) { return std::to_string(x); }
inline string repr(float x) { return std::to_string(x); }
inline string repr(string x) { return x; }
inline string repr(bool x) { return x ? "true" : "false"; }
inline string repr(nil x) { return "nil"; }
inline string repr(MathType x) { return "class 'Math'"; }
inline string repr(SystemType x) { return "class 'System'"; }
inline string repr(SplikitType x) { return "class 'Splikit'"; }
// inline string repr(IntegerType x) { return "class 'Integer'"; }

inline bool to_bool(int x) { return x > 0; }
inline bool to_bool(float x) { return x > 0; }
inline bool to_bool(string x) { return x != ""; }
inline bool to_bool(bool x) { return x; }
inline bool to_bool(nil x) { return false; }
inline bool to_bool(MathType x) { return false; }
inline bool to_bool(SystemType x) { return false; }
inline bool to_bool(SplikitType x) { return false; }
// inline bool to_bool(IntegerType x) { return false; }

inline int add(int x, int y) { return x + y; }
inline float add(float x, float y) { return x + y; }
inline string add(string x, string y) { return x + y; }

inline int sub(int x, int y) { return x - y; }
inline float sub(float x, float y) { return x - y; }

inline int mul(int x, int y) { return x * y; }
inline float mul(float x, float y) { return x * y; }

inline float div(float x, float y) { return x / y; }

inline int mod(int x, int y) { return x % y; }
inline float mod(float x, float y) { return std::fmod(x, y); }

inline bool eq(int x, int y) { return x == y; }
inline bool eq(float x, float y) { return x == y; }
inline bool eq(string x, string y) { return x == y; }

inline bool neq(int x, int y) { return x != y; }
inline bool neq(float x, float y) { return x != y; }
inline bool neq(string x, string y) { return x != y; }

inline bool lt(int x, int y) { return x < y; }
inline bool lt(float x, float y) { return x < y; }
inline bool lt(string x, string y) { return x.length() < y.length(); }

inline bool lte(int x, int y) { return x <= y; }
inline bool lte(float x, float y) { return x <= y; }
inline bool lte(string x, string y) { return x.length() <= y.length(); }

inline bool gt(int x, int y) { return x > y; }
inline bool gt(float x, float y) { return x > y; }
inline bool gt(string x, string y) { return x.length() > y.length(); }

inline bool gte(int x, int y) { return x >= y; }
inline bool gte(float x, float y) { return x >= y; }
inline bool gte(string x, string y) { return x.length() >= y.length(); }

inline bool and_(bool x, bool y) { return x && y; }

inline bool or_(bool x, bool y) { return x || y; }

inline bool not_(bool x) { return !x; }
string not_(string x) {
    string res = x;
    std::reverse(res.begin(), res.end());
    return res;
}

nil print(string x) {
    std::cout << x << '\n';
    return nullptr;
}

string input(string prompt) {
    string res;
    std::cout << prompt;
    std::getline(std::cin, res);
    return res;
}

string input() {
    string res;
    std::getline(std::cin, res);
    return res;
}

// property
inline int string_length(string s) { return s.length(); }
// property
inline string string_start(string s) { return s.substr(0, 1); }
// property
inline string string_end(string s) { return s.substr(s.length() - 1); }
// property
string string_lowered(string s) {
    string res = s;
    std::transform(res.begin(), res.end(), res.begin(), ::tolower);
    return res;
}
// property
string string_uppered(string s) {
    string res = s;
    std::transform(res.begin(), res.end(), res.begin(), ::toupper);
    return res;
}
// property
inline bool string_is_empty(string s) { return s.length() == 0; }
// method
inline string string_replace(string s, string from, string to) {
    size_t pos = 0;
    while ((pos = s.find(from, pos)) != string::npos) {
        s.replace(pos, from.length(), to);
        pos += to.length();
    }
    return s;
}
// method
inline string string_at(string s, int index) {
    if (index < 0) {
        index = s.length() + index;
    }

    if (index < 0 || index >= s.length()) {
        return "";
    }

    return s.substr(index, 1);
}
// method
inline int string_parse_int(string s) { return std::stoi(s); }
// method
inline float string_parse_float(string s) { return std::stof(s); }
// method
inline bool string_parse_bool(string s) { return s == "true" ? true : false; }

// property static
inline float Math_pi() { return PI; }
// method static
inline float Math_abs(float x) { return std::abs(x); }
// method static
inline float Math_sqrt(float x) { return std::sqrt(x); }
// method static
inline float Math_sin(float x) { return std::sin(x); }
// method static
inline float Math_cos(float x) { return std::cos(x); }
// method static
inline float Math_tan(float x) { return std::tan(x); }
// method static
inline float Math_atan(float x) { return std::atan(x); }
// method static
inline float Math_atan2(float x, float y) { return std::atan2(x, y); }
// method static
inline float Math_log(float x) { return std::log(x); }
// method static
inline float Math_log10(float x) { return std::log10(x); }
// method static
inline float Math_exp(float x) { return std::exp(x); }
// method static
inline float Math_pow(float x, float y) { return std::pow(x, y); }
// method static
inline float Math_round(float x) { return std::round(x); }
// method static
inline float Math_floor(float x) { return std::floor(x); }
// method static
inline float Math_ceil(float x) { return std::ceil(x); }
// method static
inline float Math_trunc(float x) { return std::trunc(x); }
// method static
inline float Math_hypot(float x, float y) { return std::hypot(x, y); }
// method static
inline float Math_degrees(float x) { return x * 180.0f / PI; }
// method static
inline float Math_radians(float x) { return x * PI / 180.0f; }
// method static
inline float Math_min(float x, float y) { return std::min(x, y); }
// method static
inline float Math_max(float x, float y) { return std::max(x, y); }
// method static
inline float Math_clamp(float x, float min, float max) { return std::clamp(x, min, max); }

// property static
inline string System_platform() {
#ifdef OS_WINDOWS
    return "Windows";
#elif defined(OS_UNIX)
    return "Unix";
#else
    return "Unknown";
#endif
}
// property static
inline int System_pid() {
#ifdef OS_WINDOWS
    return (int)GetCurrentProcessId();
#elif defined(OS_UNIX)
    return getpid();
#else
    return -1;
#endif
}
// property static
inline string System_cd() { return std::filesystem::current_path().string(); }
// method static
inline int System_shell(string cmd) { return system(cmd.c_str()); }
// method static
inline nil System_exit(int x) { exit(x); return nullptr; }
// method static
inline nil System_exit() { exit(0); return nullptr; }

// property static
inline string Splikit_version() {
    return VERSION;
}
