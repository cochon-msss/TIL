# Spring 주요 어노테이션

## Bean 등록 관련
- `@Component` : 개발자가 생성한 Class를 Spring의 Bean으로 등록할 때 사용
- `@ComponentScan` : `@Component`, `@Service`, `@Repository`, `@Controller`, `@Configuration` 중 하나라도 등록된 클래스를 찾으면 Context에 bean으로 등록해준다
- `@Bean` : 개발자가 제어 불가능한 외부 라이브러리 같은 것들을 Bean으로 만들 때 사용
- `@Autowired` : Bean 객체를 주입받기 위해 사용. 주입 방법은 크게 필드, 세터, 생성자가 있다. (Type을 먼저 확인 후 없으면 Name을 확인하여 주입)

## Controller 관련
- `@Controller` : 해당 Class가 Controller 역할을 한다고 Spring에게 명시
- `@RequestHeader(value="")` : Request의 header 값을 가져올 수 있으며, 메서드의 파라미터에 사용
- `@RequestMapping(value="", method=RequestMethod.POST)` : 요청 들어온 URL과 value 값이 일치하면 해당 클래스나 메서드가 실행된다. Controller 객체 안의 메서드와 클래스에 적용 가능
- `@RequestParam` : URL에 전달되는 파라미터를 메서드의 인자와 매칭시켜 받아서 처리
- `@RequestBody` : Body에 전달되는 데이터를 메서드의 인자와 매칭시켜 받아서 처리
- `@ModelAttribute`
- `@ResponseBody`
- `@GetMapping` : `@RequestMapping(method=RequestMethod.GET)`과 동일한 역할
- `@PostMapping` : `@RequestMapping(method=RequestMethod.POST)`과 동일한 역할

## Lombok 주요 어노테이션
- `@Setter` : Class 모든 필드의 Setter method를 생성
- `@Getter` : Class 모든 필드의 Getter method를 생성
- `@AllArgsConstructor` : Class 모든 필드 값을 파라미터로 받는 생성자를 추가
- `@NoArgsConstructor` : Class 기본 생성자를 자동으로 추가
- `@ToString` : Class 모든 필드의 toString method를 생성
