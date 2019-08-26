import java.util.Stack;

public class Stack2 {
    private Stack<Integer> stackData;
    private Stack<Integer> stackMin;

    public Stack2() {
        this.stackData = new Stack<>();
        this.stackMin = new Stack<>();
    }

    public void push(int newNum) {
        if (this.stackMin.isEmpty()) {
            this.stackMin.push(newNum);
        }
        else if (newNum <= this.getMin()) {
            this.stackMin.push(newNum);
        }
        else {
            this.stackMin.push(this.getMin());
        }
    }

    public int pop() {
        if (this.stackData.isEmpty()) {
            throw RuntimeException("Your stack is empty");
        }
        int value = this.stackData.pop();
        this.stackMin.pop();
        return value;
    }

    public int getMin() {
        if (this.stackData.isEmpty()) {
            throw RuntimeException("Your stack is empty");
        }
        return this.stackMin.peek();
    }
}