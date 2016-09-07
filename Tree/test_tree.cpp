/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-09-07 08:42:12
 */
#include <iostream>
#include "tree.h"
#include <vector>
using namespace std;

int main() {
    Tree demo;
    /*
          1
        /   \
       2     3
       \    / \
       4   5   6
      / \
     7  8
    */
    demo.deserialize("1 2 3 null 4 5 6 7 8");
    cout << demo.serialize() << endl;
    cout << demo.pre_order_r(demo.get_root()) << endl;
    cout << demo.pre_order_i(demo.get_root()) << endl;

    cout << demo.post_order_r(demo.get_root()) << endl;
    cout << demo.post_order_i(demo.get_root()) << endl;

    cout << demo.in_order_r(demo.get_root()) << endl;
    cout << demo.in_order_i(demo.get_root()) << endl;
}

