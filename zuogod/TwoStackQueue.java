import java.util.stack;

public class TwoStackQueue {
    private Stack<Integer> stackPush;
    private Stack<Integer> stackPop;

    public TwoStackQueue() {
        this.stackPush = new Stack<>();
        this.stackPop = new Stack<>();
    }

    public void add(int newNum) {
        this.stackPush.push(newNum);
    }

    public int poll() {
        if (this.stackPush.empty() && this.stackPop.empty()) {
            throw RuntimeException("Your queue is empty");
        }
        else if (this.stackPop.empty()) {
            this.move();
        }
        return this.stackPop.pop();
    }

    public int peek() {
        if (this.stackPush.empty() && this.stackPop.empty()) {
            throw RuntimeException("Your queue is empty");
        }
        else if (this.stackPop.empty()) {
            this.move();
        }
        return this.stackPop.peek();
    }

    private void move() {
        while(!this.stackPush.empty()) {
            this.stackPop.push(this.stackPush.pop());
        }
    }
}