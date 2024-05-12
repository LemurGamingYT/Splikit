#pragma once

#include "../splikit.hpp"

#include <fstream>


struct FileType {
    std::fstream f;
    std::filesystem::path p;
    string path;
};

#define File FileType


inline string type(File& _) { return "File"; }

inline string repr(File& f) { return "File(path='" + f.path + "')"; }

// function, single-return({std::fstream(@1@),std::filesystem::path(@1@),@1@})
File open_file(string path) { return {std::fstream(path), std::filesystem::path(path), path}; }


// property, single-return(@1@.path)
inline string File_path(File& f) { return f.path; }

// property, single-return(std::filesystem::is_regular_file(@1@.p))
inline bool File_is_file(File& f) { return std::filesystem::is_regular_file(f.p); }

// property, single-return(std::filesystem::is_directory(@1@.p))
inline bool File_is_dir(File& f) { return std::filesystem::is_directory(f.p); }

// property, single-return(std::filesystem::exists(@1@.p))
inline bool File_exists(File& f) { return std::filesystem::exists(f.p); }

// single-return(File_exists(@1@))
inline bool to_bool(File& f) { return File_exists(f); }

// single-return(!File_exists(@1@))
inline bool not_(File& f) { return !to_bool(f); }

// property
string File_content(File& f) {
    if (!File_exists(f)) throw splikit_error("File does not exist");
    if (!File_is_file(f)) throw splikit_error("File is not a file");

    std::ifstream file(f.path);
    string out = string((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();
    return out;
}

// property
int File_size(File& f) {
    if (!File_exists(f)) throw splikit_error("File does not exist");
    if (!File_is_file(f)) throw splikit_error("File is not a file");
    return std::filesystem::file_size(f.p);
}

// method
inline nil File_close(File& f) {
    f.f.close();
    return nullptr;
}

// method
nil File_write(File& f, string s) {
    if (!File_is_file(f)) throw splikit_error("File is not a file");

    f.f << s;
    return nullptr;
}

// method
nil File_create(File& f) {
    if (!File_exists(f)) {
        f.f.close();
        f.f.open(f.path, std::ios::out);
    }

    throw splikit_error("File already exists");
}
