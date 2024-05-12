#pragma once


#include <filesystem>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
#include <cmath>
#include <regex>


using nil = std::nullptr_t;
using std::string;


const string VERSION = "0.0.21";

constexpr float PI = 3.14159265358979323846;
constexpr float E = 2.71828182845904523536;
constexpr float TAU = 6.28318530717958647693;
constexpr int ONE_BILLION = 1000000000;
constexpr int ONE_MILLION = 1000000;
constexpr int ONE_THOUSAND = 1000;
constexpr int MAX_INT = 2147483647;
constexpr int MIN_INT = -2147483648;


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
#else
    #define OS_UNKNOWN
#endif


template <typename T>
struct array {
    std::vector<T> elements;

    array() = default;

    explicit array(size_t size) : elements(size) {}

    array(const array<T>& other) = default;
    array(array<T>&& other) = default;

    using iterator = typename std::vector<T>::iterator;
    iterator begin() { return elements.begin(); }
    iterator end() { return elements.end(); }
};

struct regex {
    string pattern;
    std::regex r;
};


class splikit_error : public std::exception {
private:
    string message;
public:
    const char* what() const noexcept override { return message.c_str(); }
    splikit_error(string msg) : message(msg) {}
};


struct MathType{};
#define Math MathType{}

struct SystemType{};
#define System SystemType{}

struct SplikitType{};
#define Splikit SplikitType{}


// single-return("int")
inline string type(int _) { return "int"; }
// single-return("float")
inline string type(float _) { return "float"; }
// single-return("string")
inline string type(string _) { return "string"; }
// single-return("bool")
inline string type(bool _) { return "bool"; }
// single-return("nil")
inline string type(nil _) { return "nil"; }
// single-return("Math")
inline string type(MathType _) { return "Math"; }
// single-return("System")
inline string type(SystemType _) { return "System"; }
// single-return("Splikit")
inline string type(SplikitType _) { return "Splikit"; }
template <typename T>
// single-return("array")
inline string type(array<T> _) { return "array"; }
// single-return("regex")
inline string type(regex _) { return "regex"; }

// single-return(std::to_string(@1@))
inline string repr(int x) { return std::to_string(x); }
// single-return(std::to_string(@1@))
inline string repr(float x) { return std::to_string(x); }
// single-return(std::to_string(@1@))
inline string repr(string x) { return x; }
// single-return(@1@ ? "true" : "false")
inline string repr(bool x) { return x ? "true" : "false"; }
// single-return("nil")
inline string repr(nil x) { return "nil"; }
// single-return("class 'Math'")
inline string repr(MathType x) { return "class 'Math'"; }
// single-return("class 'System'")
inline string repr(SystemType x) { return "class 'System'"; }
// single-return("class 'Splikit'")
inline string repr(SplikitType x) { return "class 'Splikit'"; }
template <typename T>
string repr(array<T> x) {
    std::ostringstream oss;
    oss << '{';
    for (const auto& element : x.elements) {
        oss << repr(element);
        if (&element != &x.elements.back()) oss << ", ";
    }

    oss << '}';
    return oss.str();
}
// single-return(@1@.pattern)
inline string repr(regex x) { return x.pattern; }

// single-return(@1@>0)
inline bool to_bool(int x) { return x > 0; }
// single-return(@1@>0)
inline bool to_bool(float x) { return x > 0; }
// single-return(@1@!="")
inline bool to_bool(string x) { return x != ""; }
// single-return(@1@)
inline bool to_bool(bool x) { return x; }
// single-return(false)
inline bool to_bool(nil x) { return false; }
// single-return(false)
inline bool to_bool(MathType x) { return false; }
// single-return(false)
inline bool to_bool(SystemType x) { return false; }
// single-return(false)
inline bool to_bool(SplikitType x) { return false; }
template <typename T>
// single-return(@1@.elements.size()>0)
inline bool to_bool(array<T> x) { return x.elements.size() > 0; }
inline bool to_bool(regex x) {
    try {
        std::regex r(x.pattern);
        return true;
    } catch (const std::regex_error& e) {
        return false;
    }

    return false;
}

// single-return(@1@+@2@)
inline int add(int x, int y) { return x + y; }
// single-return(@1@+@2@)
inline float add(float x, float y) { return x + y; }
// single-return(@1@+@2@)
inline string add(string x, string y) { return x + y; }
template <typename T>
array<T> add(const array<T>& a, const array<T>& b) {
    array<T> result;
    result.elements.reserve(a.elements.size() + b.elements.size());
    std::copy(a.elements.begin(), a.elements.end(), std::back_inserter(result.elements));
    std::copy(b.elements.begin(), b.elements.end(), std::back_inserter(result.elements));
    return std::move(result);
}

// single-return(@1@-@2@)
inline int sub(int x, int y) { return x - y; }
// single-return(@1@-@2@)
inline float sub(float x, float y) { return x - y; }

// single-return(@1@*@2@)
inline int mul(int x, int y) { return x * y; }
// single-return(@1@*@2@)
inline float mul(float x, float y) { return x * y; }

// single-return(@1@/@2@)
inline float div(float x, float y) { return x / y; }

// single-return(@1@%@2@)
inline int mod(int x, int y) { return x % y; }
// single-return(std::fmod(@1@,@2@))
inline float mod(float x, float y) { return std::fmod(x, y); }
inline string mod(int x, string y) {
    if (x > y.length()) x = y.length();
    return y.substr(0, x);
}
inline string mod(string x, int y) {
    if (y > x.length()) y = x.length();
    return x.substr(x.length() - y, y);
}

// single-return(@1@==@2@)
inline bool eq(int x, int y) { return x == y; }
// single-return(@1@==@2@)
inline bool eq(float x, float y) { return x == y; }
// single-return(@1@==@2@)
inline bool eq(string x, string y) { return x == y; }
// single-return(@1@==@2@)
inline bool eq(bool x, bool y) { return x == y; }
template <typename T>
// single-return(std::equal(@1@.elements.begin(),@1@.elements.end(),@2@.elements.begin()))
inline bool eq(const array<T>& x, const array<T>& y) { return std::equal(x.elements.begin(), x.elements.end(), y.elements.begin()); }

// single-return(@1@!=@2@)
inline bool neq(int x, int y) { return x != y; }
// single-return(@1@!=@2@)
inline bool neq(float x, float y) { return x != y; }
// single-return(@1@!=@2@)
inline bool neq(string x, string y) { return x != y; }
// single-return(@1@!=@2@)
inline bool neq(bool x, bool y) { return x != y; }
template <typename T>
inline bool neq(const array<T>& x, const array<T>& y) { return std::not_equal_to<T>()(x.elements.begin(), x.elements.end(), y.elements.begin()); }

// single-return(@1@<@2@)
inline bool lt(int x, int y) { return x < y; }
// single-return(@1@<@2@)
inline bool lt(float x, float y) { return x < y; }
// single-return(@1@.length()<@2@.length())
inline bool lt(string x, string y) { return x.length() < y.length(); }
template <typename T>
// single-return(@1@.elements.size()<@2@.elements.size())
inline bool lt(array<T> x, array<T> y) { return x.elements.size() < y.elements.size(); }

// single-return(@1@<=@2@)
inline bool lte(int x, int y) { return x <= y; }
// single-return(@1@<=@2@)
inline bool lte(float x, float y) { return x <= y; }
// single-return(@1@.length()<=@2@.length())
inline bool lte(string x, string y) { return x.length() <= y.length(); }
template <typename T>
// single-return(@1@.elements.size()<=@2@.elements.size())
inline bool lte(array<T> x, array<T> y) { return x.elements.size() <= y.elements.size(); }

// single-return(@1@>@2@)
inline bool gt(int x, int y) { return x > y; }
// single-return(@1@>@2@)
inline bool gt(float x, float y) { return x > y; }
// single-return(@1@.length()>@2@.length())
inline bool gt(string x, string y) { return x.length() > y.length(); }
template <typename T>
// single-return(@1@.elements.size()>@2@.elements.size())
inline bool gt(array<T> x, array<T> y) { return x.elements.size() > y.elements.size(); }

// single-return(@1@>=@2@)
inline bool gte(int x, int y) { return x >= y; }
// single-return(@1@>=@2@)
inline bool gte(float x, float y) { return x >= y; }
// single-return(@1@.length()>=@2@.length())
inline bool gte(string x, string y) { return x.length() >= y.length(); }
template <typename T>
// single-return(@1@.elements.size()>=@2@.elements.size())
inline bool gte(array<T> x, array<T> y) { return x.elements.size() >= y.elements.size(); }

// single-return(@1@ && @2@)
inline bool and_(bool x, bool y) { return x && y; }

// single-return(@1@||@2@)
inline bool or_(bool x, bool y) { return x || y; }

// single-return(!@1@)
inline bool not_(bool x) { return !x; }
string not_(string x) {
    std::reverse(x.begin(), x.end());
    return x;
}

nil print(string x) {
    std::cout << x << std::endl;
    return nullptr;
}

string input(string prompt) {
    string res;
    std::cout << prompt;
    std::getline(std::cin, res);
    if (!std::cin) {
        throw splikit_error("Input failed");
    }
    return res;
}

string input() {
    string res;
    std::getline(std::cin, res);
    if (!std::cin) {
        throw splikit_error("Input failed");
    }
    return res;
}

array<int> range(int start, int end) {
    array<int> res(end - start);
    std::iota(res.elements.begin(), res.elements.end(), start);
    return res;
}

array<int> range(int end) {
    array<int> res(end);
    std::iota(res.elements.begin(), res.elements.end(), 0);
    return res;
}

array<int> range(int start, int end, int step) {
    array<int> res;
    for (int i = start; i < end; i += step) {
        res.elements.push_back(i);
    }
    return res;
}


// property, single-return((int)@1@.length())
inline int string_length(string s) { return s.length(); }

// property, single-return(@1@.substr(0,1))
inline string string_start(string s) { return s.substr(0, 1); }

// property, single-return(@1@.substr(@1@.length()-1))
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

// property, single-return(@1@.length()==0)
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
        throw splikit_error("Index out of range");
    }

    return s.substr(index, 1);
}

// method
inline int string_parse_int(string s) {
    try {
        return std::stoi(s);
    } catch (const std::invalid_argument& e) {
        throw splikit_error("Invalid integer value" + s);
    }
}

// method
inline float string_parse_float(string s) {
    try {
        return std::stof(s);
    } catch (const std::invalid_argument& e) {
        throw splikit_error("Invalid float value" + s);
    }
}

// method
inline bool string_parse_bool(string s) {
    if (s == "true" || s == "false") {
        return s == "true";
    }

    throw splikit_error("Invalid boolean value" + s);
}

template <typename T>
string string_join(const string s, const array<T>& x) {
    string res = "";
    res.reserve(x.elements.size() * (s.length() + 1));
    for (const auto& element : x.elements) {
        res.append(element);
        if (&element != &x.elements.back()) {
            res.append(s);
        }
    }
    return res;
}

// method
array<string> string_split(string s, string delimiter) {
    array<string> res;
    res.elements.reserve(s.length() / delimiter.length() + 1);
    size_t pos = 0;
    std::string_view token;
    size_t start = 0;
    do {
        pos = s.find(delimiter, start);
        token = std::string_view(s.data() + start, pos - start);
        res.elements.emplace_back(string(token));
        start = pos + delimiter.length();
    } while (pos != string::npos);
    res.elements.emplace_back(s.substr(start));
    return res;
}


template <typename T>
array<T> new_array(const std::vector<T>& elements) {
    array<T> res;
    res.elements = elements;
    return res;
}


template <typename T>
// property, single-return((int)@1@.elements.size())
inline int array_length(array<T> x) { return x.elements.size(); }

template <typename T>
// property, single-return(@1@.elements[0])
inline T array_first(array<T> x) { return x.elements[0]; }

template <typename T>
// property, single-return(@1@.elements[@1@.elements.size() - 1])
inline T array_last(array<T> x) { return x.elements[x.elements.size() - 1]; }

template <typename T>
// property
inline string array_type(array<T> x) { return type(T()); }

template <typename T>
// method, single-return(@1@.elements[@2@])
inline T array_at(array<T> x, int index) { return x.elements[index]; }

template <typename T>
// method
inline nil array_add(array<T>& x, T element) {
    x.elements.push_back(element);
    return nullptr;
}

template <typename T>
// method
inline nil array_remove(array<T>& x, int index) {
    x.elements.erase(x.elements.begin() + index);
    return nullptr;
}

/*// method
template <typename T>
(T) array_pop(array<T>& x, int index = -1) {
    if (index == -1) {
        index = x.elements.empty() ? 0 : x.elements.size() - 1;
    }

    if (index < 0 || index >= x.elements.size()) {
        throw splikit_error("Index out of range");
    }

    T res = std::move(x.elements[index]);
    std::swap(x.elements[index], x.elements.back());
    x.elements.pop_back();
    return res;
}*/

template <typename T>
// method
inline nil array_sort(array<T>& x) {
    std::sort(x.elements.begin(), x.elements.end());
    return nullptr;
}

/*template <typename T>
// method
(nil) array_sort(array<T>& x, bool reverse) {
    if (reverse) {
        std::sort(x.elements.begin(), x.elements.end(), std::greater<T>());
    } else {
        std::sort(x.elements.begin(), x.elements.end());
    }
    return nullptr;
}*/

template <typename T>
// method
inline nil array_reverse(array<T>& x) {
    std::reverse(x.elements.begin(), x.elements.end());
    return nullptr;
}


inline regex new_regex(string pattern) {
    std::regex r(pattern);
    return regex{pattern, r};
}


// property, single-return(@1@.pattern)
inline string regex_pattern(regex r) { return r.pattern; }

// method, single-return(std::regex_match(@2@,@1@.r))
inline bool regex_has_match(regex r, string s) { return std::regex_match(s, r.r); }

// method, single-return(std::regex_replace(@2@,@1@.r,@3@))
inline string regex_replace(regex r, string s, string replacement) { return std::regex_replace(s, r.r, replacement); }

// method, single-return(std::regex_replace(@2@,@1@.r,@3@,std::regex_constants::format_first_only))
inline string regex_replace_all(regex r, string s, string replacement) { return std::regex_replace(s, r.r, replacement, std::regex_constants::format_first_only); }

// method, single-return(std::regex_search(@2@,@1@.r)?@1@.pattern:string())
inline string regex_find(regex r, string s) { return std::regex_search(s, r.r) ? r.pattern : string(); }


// property, static, single-return((float)PI)
inline float Math_pi() { return PI; }

// property, static, single-return((float)E)
inline float Math_e() { return E; }

// property, static, single-return((float)INFINITY)
inline float Math_infinity() { return INFINITY; }

// property, static, single-return((float)NAN)
inline float Math_nan() { return NAN; }

// property, static, single-return((float)TAU)
inline float Math_tau() { return TAU; }

// method, static, single-return(std::abs(@1@))
inline float Math_abs(float x) { return std::abs(x); }

// method, static, single-return(std::sqrt(@1@))
inline float Math_sqrt(float x) { return std::sqrt(x); }

// method, static, single-return(std::sin(@1@))
inline float Math_sin(float x) { return std::sin(x); }

// method, static, single-return(std::cos(@1@))
inline float Math_cos(float x) { return std::cos(x); }

// method, static, single-return(std::tan(@1@))
inline float Math_tan(float x) { return std::tan(x); }

// method, static, single-return(std::asin(@1@))
inline float Math_atan(float x) { return std::atan(x); }

// method, static, single-return(std::atan2(@1@,@2@))
inline float Math_atan2(float x, float y) { return std::atan2(x, y); }

// method, static, single-return(std::log(@1@))
inline float Math_log(float x) { return std::log(x); }

// method, static, single-return(std::log10(@1@))
inline float Math_log10(float x) { return std::log10(x); }

// method, static, single-return(std::exp(@1@))
inline float Math_exp(float x) { return std::exp(x); }

// method, static, single-return(std::pow(@1@,@2@))
inline float Math_pow(float x, float y) { return std::pow(x, y); }

// method, static, single-return(std::round(@1@))
inline float Math_round(float x) { return std::round(x); }

// method, static, single-return(std::floor(@1@))
inline float Math_floor(float x) { return std::floor(x); }

// method, static, single-return(std::ceil(@1@))
inline float Math_ceil(float x) { return std::ceil(x); }

// method, static, single-return(std::trunc(@1@))
inline float Math_trunc(float x) { return std::trunc(x); }

// method, static, single-return(std::hypot(@1@,@2@))
inline float Math_hypot(float x, float y) { return std::hypot(x, y); }

// method, static, single-return(@1@*180.0f/PI)
inline float Math_degrees(float x) { return x * 180.0f / PI; }

// method, static, single-return(@1@*PI/180.0f)
inline float Math_radians(float x) { return x * PI / 180.0f; }

// method, static, single-return(std::min(@1@,@2@))
inline float Math_min(float x, float y) { return std::min(x, y); }

// method, static, single-return(std::max(@1@,@2@))
inline float Math_max(float x, float y) { return std::max(x, y); }

// method, static, single-return(std::clamp(@1@,@2@,@3@))
inline float Math_clamp(float x, float min, float max) { return std::clamp(x, min, max); }

// method, static, single-return(std::rand()%(@2@-@1@+1)+@1@)
inline int Math_random_int(int min, int max) { return std::rand() % (max - min + 1) + min; }

// method, static
int Math_factorial(int x) {
    if (x <= 1) {
        return 1;
    } else {
        return x * Math_factorial(x - 1);
    }
}

// method, static
float Math_mean(array<float> numbers) {
    float sum = 0.0f;
    for (float num : numbers.elements) {
        sum += num;
    }

    return sum / numbers.elements.size();
}

// method, static
int Math_mean(array<int> numbers) {
    int sum = 0;
    for (int num : numbers.elements) {
        sum += num;
    }

    return sum / numbers.elements.size();
}

// method, static
float Math_variance(array<float> numbers) {
    float mean = Math_mean(numbers);
    float sumOfSquares = 0.0f;
    for (float num : numbers.elements) {
        sumOfSquares += (num - mean) * (num - mean);
    }

    return sumOfSquares / numbers.elements.size();
}

// method, static
int Math_variance(array<int> numbers) {
    int mean = Math_mean(numbers);
    int sumOfSquares = 0;
    for (int num : numbers.elements) {
        sumOfSquares += (num - mean) * (num - mean);
    }

    return sumOfSquares / numbers.elements.size();
}

// method, static
array<float> Math_linear_regression(array<float> x, array<float> y) {
    float sumX = std::accumulate(x.elements.begin(), x.elements.end(), 0.0f);
    float sumY = std::accumulate(y.elements.begin(), y.elements.end(), 0.0f);
    float sumXY = std::inner_product(x.elements.begin(), x.elements.end(), y.elements.begin(), 0.0f);
    float sumX2 = std::inner_product(x.elements.begin(), x.elements.end(), x.elements.begin(), 0.0f);
    float n = x.elements.size();
    float m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    float b = (sumY - m * sumX) / n;
    std::vector<float> ret;
    ret.push_back(m);
    ret.push_back(b);
    return new_array(ret);
}

// method, static
array<int> Math_linear_regression(array<int> x, array<int> y) {
    float sumX = std::accumulate(x.elements.begin(), x.elements.end(), 0.0f);
    float sumY = std::accumulate(y.elements.begin(), y.elements.end(), 0.0f);
    float sumXY = std::inner_product(x.elements.begin(), x.elements.end(), y.elements.begin(), 0.0f);
    float sumX2 = std::inner_product(x.elements.begin(), x.elements.end(), x.elements.begin(), 0.0f);
    float n = x.elements.size();
    float m = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    float b = (sumY - m * sumX) / n;
    std::vector<int> ret;
    ret.push_back(m);
    ret.push_back(b);
    return new_array(ret);
}


// property, static
inline string System_platform() {
#ifdef OS_WINDOWS
    return "Windows";
#elif defined(OS_UNIX)
    return "Unix";
#else
    return "Unknown";
#endif
}

// property, static
inline int System_pid() {
#ifdef OS_WINDOWS
    return (int)GetCurrentProcessId();
#elif defined(OS_UNIX)
    return getpid();
#else
    throw splikit_error("Unsupported platform");
#endif
}

// property, static, single-return(std::filesystem::current_path().string())
inline string System_cd() { return std::filesystem::current_path().string(); }

// method, static
inline int System_shell(string cmd) { return system(cmd.c_str()); }

// method, static
inline nil System_exit(int x) { exit(x); return nullptr; }

// method, static
inline nil System_exit() { exit(0); return nullptr; }

// // method, static
// inline nil System_disable_keyboard() {
// #ifdef OS_WINDOWS
//     BlockInput(true);
// #else
//     throw splikit_error("Unsupported platform");
// #endif
//     return nullptr;
// }

// // method, static
// inline nil System_enable_keyboard() {
// #ifdef OS_WINDOWS
//     BlockInput(false);
// #else
//     throw splikit_error("Unsupported platform");
// #endif
//     return nullptr;
// }

// // method, static
// inline nil System_disable_mouse() {
// #ifdef OS_WINDOWS
//     ShowCursor(false);
// #else
//     throw splikit_error("Unsupported platform");
// #endif
//     return nullptr;
// }

// // method, static
// inline nil System_enable_mouse() {
// #ifdef OS_WINDOWS
//     ShowCursor(true);
// #else
//     throw splikit_error("Unsupported platform");
// #endif
//     return nullptr;
// }

// // method, static
// inline bool System_is_key_pressed(string key) {
// #ifdef OS_WINDOWS
//     if (key.length() > 1) {
//         throw splikit_error("Invalid key, expected a single character");
//     }

//     return GetAsyncKeyState((int)key[0]) & 0x8000;
// #else
//     throw splikit_error("Unsupported platform");
// #endif
// }


// property, static, single-return(VERSION)
inline string Splikit_version() { return VERSION; }
