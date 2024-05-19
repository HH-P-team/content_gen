import "./Subjects.css";
import Card from "../Card/Card";
import getAllSubjects from "../../api/subjects/subject.api";
import { useState, useEffect } from 'react';

export default function Subjects(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    getAllSubjects().then((data) => {
      if (data.status) {
        setData(data.result);
      }
    });
  }, []);

  return (
    <div>
      <h2>Категории продуктов</h2>
      <div className="Subjects">
        {props.data.map((elem) => (
          <Card name={elem.name} key={elem.id} />
        ))}
      </div>
    </div>
  );
}
