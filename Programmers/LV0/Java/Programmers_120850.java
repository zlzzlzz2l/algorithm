import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * fileName       : Programmers_120850
 * author         : AHyun Kim
 * date           : 2023-01-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-02        AHyun Kim          최초 생성
 */
public class Programmers_120850 {
    public static void main(String[] args) {
        Programmers_120850 s = new Programmers_120850();

        String my_string = "p2o4i8gj2";

        System.out.println(s.solution(my_string));
    }

    public List<Integer> solution(String my_string) {
        List<Integer> answer = new LinkedList<>();

        for (String myStr : my_string.split("")) {
            if (myStr.matches("[0-9]")) {
                answer.add(Integer.valueOf(myStr));
            }
        }

        Collections.sort(answer);

        return answer;
    }
}
