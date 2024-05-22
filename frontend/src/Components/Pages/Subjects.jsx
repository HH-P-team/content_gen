import { useState, useEffect } from "react";
import "./Subjects.css";
import PageWrapper from "./PageWrapper";
import getAllSubjects from "../../api/subjects/subject.api";
import Card from "../Card/Card";
import Button from "../Button/Button";

export default function Subjects(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    getAllSubjects().then((data) => {
      if (data.status) {
        setData(data.result);
        // console.log(data.result);
      }
    });
  }, []);

  return (
    <PageWrapper
      pageName={"Категории продуктов"}
      controlElement={
        <Button name={"Добавить"} action={() => console.log("trololo")} />
      }
      content={
        <div className="Subjects">
          {data.map((elem) => (
            <Card name={elem.name} key={elem.id} id={elem.id} />
          ))}
        </div>
      }
    />
  );
}
