public class Programmers_120845 {
    public static void main(String[] args) {
        Programmers_120845 s = new Programmers_120845();

        int[] box = {10, 8, 6};
        int n = 3;

        System.out.println(s.solution(box, n));
    }

    public int solution(int[] box, int n) {
        int answer = 0;

        int one = box[0] / n;
        int two = box[1] / n;
        int three = box[2] / n;

        answer = one * two * three;

        return answer;
    }
}