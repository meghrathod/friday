import "../App.css"
import Navbar from "../components/Navbar";
import CardContainer from "../components/CardContainer";

const Dashboard = (props) => {

    const { students, totalMarks, totalTestCases } = props.data


    const marksArray = students.map((student) => {
        return student.totalMarks
    })

    const testCasesArray = students.map((student) => {
        return student.testcasesPassed
    })

    const data = {
        labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        datasets: [
            { values: [18, 40, 30, 35, 8, 52, 17, -4] }
        ]
    }


    return (
        <div className="Dashboard">
            <Navbar />
            <CardContainer data={props.data} />
            

        </div>
    )
}

export default Dashboard;