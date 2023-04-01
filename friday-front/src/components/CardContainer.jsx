import { Card } from "react-bootstrap"


const CardContainer = (props) => {

    const { students, totalMarks, totalTestCases } = props.data

    // students is an array of objects of the form for example:
    // {
    //     "roll": "123",
    //     "testcasesPassed": "2",
    //     "totalMarks": "5",
    // }

    const marksArray = students.map((student) => {
        return student.totalMarks
    })

    const maxMarks = Math.max(...marksArray)
    const minMarks = Math.min(...marksArray)
    const avgMarks = totalMarks / students.length

    const testCasesArray = students.map((student) => {
        return student.testcasesPassed
    })

    const avgTestCases = totalTestCases / students.length

    const analysis = {
        "Maximum Marks": maxMarks,
        "Minimum Marks": minMarks,
        "Average Marks": avgMarks,
        "Avg. No. of Testcase": avgTestCases
    }

    return (
        <div className="card-container">
            {Object.entries(analysis).map((analysis) => {
                return (
                    <Card className="card-size">
                        <Card.Body>
                            <Card.Text className="card-text">{analysis[0]}</Card.Text>
                            <Card.Title className="card-title">
                                {analysis[1]}
                            </Card.Title>
                        </Card.Body>
                    </Card>
                )
            }
            )}
        </div>
    );
};

export default CardContainer;