#pragma once

#include "../splikit.hpp"

#include <chrono>
#include <thread>


/*struct DateTimeType {
    struct tm t;
};

#define DateTime DateTimeType


inline string type(DateTime _) { return "DateTime"; }

inline string repr(DateTime x) {
    return "DateTime(" + std::to_string(x.t.tm_year) + ")";
}

inline bool to_bool(DateTime x) { return false; }


// function
DateTime dt_now() {
    struct tm t = {0};
    time_t now = time(0);
    t = *localtime(&now);
    return {t};
}

// function
DateTime dt(int year = 0, int month = 0, int day = 0, int hour = 0, int minute = 0, int second = 0) {
    struct tm t = {0};
    if (year != 0) {
        t.tm_year = year - 1900;
    }
    if (month != 0) {
        t.tm_mon = month - 1;
    }

    t.tm_mday = day;
    t.tm_hour = hour;
    t.tm_min = minute;
    t.tm_sec = second;
    return {t};
}*/

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
bool is_leap_year(int year) {
    return ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0));
}


/*DateTime add(DateTime x, DateTime y) {
    struct tm t = x.t;
    t.tm_year += y.t.tm_year;
    t.tm_mon += y.t.tm_mon;
    t.tm_mday += y.t.tm_mday;
    t.tm_hour += y.t.tm_hour;
    t.tm_min += y.t.tm_min;
    t.tm_sec += y.t.tm_sec;
    return {t};
}

DateTime sub(DateTime x, DateTime y) {
    struct tm t = x.t;
    t.tm_year -= y.t.tm_year;
    t.tm_mon -= y.t.tm_mon;
    t.tm_mday -= y.t.tm_mday;
    t.tm_hour -= y.t.tm_hour;
    t.tm_min -= y.t.tm_min;
    t.tm_sec -= y.t.tm_sec;
    return {t};
}


// property
inline int DateTime_year(DateTime x) { return x.t.tm_year; }

// property
inline int DateTime_month(DateTime x) { return x.t.tm_mon; }

// property
inline int DateTime_day(DateTime x) { return x.t.tm_mday; }

// property
inline int DateTime_hour(DateTime x) { return x.t.tm_hour; }

// property
inline int DateTime_minute(DateTime x) { return x.t.tm_min; }

// property
inline int DateTime_second(DateTime x) { return x.t.tm_sec; }

// property
inline int DateTime_weekday(DateTime x) { return x.t.tm_wday; }

// property
inline int DateTime_day_of_year(DateTime x) { return x.t.tm_yday; }

// property
inline int DateTime_isdst(DateTime x) { return x.t.tm_isdst; }*/
