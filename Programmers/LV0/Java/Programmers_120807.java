public class Programmers_120807 {
    public static void main(String[] args) {
        Programmers_120807 s = new Programmers_120807();

        int num1 = 4;
        int num2 = 3;

        System.out.println(s.solution(num1, num2));
    }

    public int solution(int num1, int num2) {
        if (num1 != num2) {
            return -1;
        } else {
            return 1;
        }
    }
}
