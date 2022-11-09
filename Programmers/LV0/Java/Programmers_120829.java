public class Programmers_120829 {
    public static void main(String[] args) {
        Programmers_120829 s = new Programmers_120829();

        int angle = 125;

        System.out.println(s.solution(angle));
    }

    public int solution(int angle) {
        int answer = 0;
        if (angle > 0 && angle < 90) {
            answer = 1;
        } else if (angle == 90) {
            answer = 2;
        } else if (angle > 90 && angle < 180) {
            answer = 3;
        } else {
            answer = 4;
        }
        return answer;
    }
}
