#pragma once

#include "../splikit.hpp"

#include <chrono>
#include <thread>


// function
nil sleep(int ms) {
    std::this_thread::sleep_for(std::chrono::milliseconds(ms));
    return nullptr;
}

// function
string formatted_time() {
    time_t now = time(0);
    struct tm tstruct;
    char buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d %X", &tstruct);
    return string(buf);
}

// function
float time_now() {
    return (float)time(0);
}
