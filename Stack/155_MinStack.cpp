/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-15 16:10:01
 */


class MinStack {
public:
    void push(int x) {
        data.push(x);
        if(min_n.empty() || x <= getMin()){
            min_n.push(x);
        }
    }

    void pop() {
        if(top() == getMin()){
            min_n.pop();
        }
        data.pop();
    }

    int top() {
        return data.top();
    }

    int getMin() {
        return min_n.top();
    }
private:
    stack<int> data;
    stack<int> min_n;
};
