#pragma once

#include "../splikit.hpp"

#include <sys/stat.h>
#include <fstream>


struct FileType {
    std::fstream f;
    std::filesystem::path p;
    string path;
};


inline string type(FileType _) { return "File"; }

inline string repr(FileType f) { return "File(path=" + f.path + ")"; }

// function
FileType open_file(string path) {
    FileType f;
    f.f.open(path);
    f.p = std::filesystem::path(path);
    f.path = path;
    return f;
}


// property
inline string File_path(FileType f) { return f.path; }

// property
inline bool File_exists(FileType& f) { return std::filesystem::exists(f.p); }

inline bool to_bool(FileType f) { return File_exists(f); }

// property
string File_content(FileType f) {
    if (!File_exists(f)) return "";

    std::ifstream file(f.path);
    string out = string((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    return out;
}

// property
inline bool File_is_file(FileType& f) { return std::filesystem::is_regular_file(f.p); }

// property
inline bool File_is_dir(FileType f) { return std::filesystem::is_directory(f.p); }

// property
int File_size(FileType f) {
    if (!File_exists(f)) return -1;
    if (!File_is_file(f)) return -1;
    return std::filesystem::file_size(f.p);
}

// method
inline nil File_close(FileType f) {
    f.f.close();
    return nullptr;
}

// method
nil File_write(FileType f, string s) {
    if (!File_is_file(f)) { return nullptr; }

    f.f << s;
    return nullptr;
}

// method
nil File_create(FileType f) {
    if (!File_exists(f)) {
        f.f.close();
        f.f.open(f.path, std::ios::out);
    }

    return nullptr;
}
