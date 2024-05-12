#pragma once

#include "../splikit.hpp"


struct RuleType {
    string name;
    std::regex r;
};

#define Rule struct RuleType

struct TokenType {
    string type;
    string value;
};

#define Token struct TokenType

struct LexerType {
    string src;
    std::vector<Rule> rules;
};

#define Lexer struct LexerType


inline string type(Lexer& _) { return "Lexer"; }
inline string type(Token& _) { return "Token"; }

inline string repr(Lexer& l) { return "Lexer(src='" + l.src + "')"; }
inline string repr(const Token& t) { return "Token(type='" + t.type + "', value='" + t.value + "')"; }

inline bool to_bool(Lexer& l) { return true; }
inline bool to_bool(Token& t) { return t.type != "EOF"; }


// function, single-return({@1@.src,std::vector<Rule>()})
inline Lexer new_lexer(string src) { return {src, std::vector<Rule>()}; }


// property, single-return(@1@.type)
inline string Token_type(Token& t) { return t.type; }

// property, single-return(@1@.value)
inline string Token_value(Token& t) { return t.value; }


// property, single-return(@1@.src)
inline string Lexer_src(Lexer& l) { return l.src; }

// method
nil Lexer_add_rule(Lexer& l, string name, regex r) {
    l.rules.push_back({name, r.r});
    return nullptr;
}

// method
array<Token> Lexer_tokenize(Lexer& l) {
    std::vector<Token> tokens;

    string::const_iterator start = l.src.begin();
    string::const_iterator end = l.src.end();
    string::const_iterator current = start;

    while (current != end) {
        bool matched = false;

        for (auto& rule : l.rules) {
            std::smatch m;
            if (std::regex_search(current, end, m, rule.r, std::regex_constants::match_continuous)) {
                tokens.push_back({rule.name, string(m[0].first, m[0].second)});
                current = m[0].second;
                matched = true;
                break;
            }
        }

        if (!matched) {
            current++;
        }
    }

    return new_array(tokens);
}
