// import { Suspense } from 'react';
import getImageByText from '../../api/images/image.api';
import './ActiveImage.css';
import { useEffect, useState } from 'react';

export default function ActiveImage(props) {

    const [data, setData] = useState([]);

    useEffect(() => {
        getImageByText(props.message).then((data) => {
            if (data.status) {
                setData(data.result);
            }
        });
    }, [data]);

    return (
        <img className="ActiveImage" src={"data:image/png;base64, " + data}/>
    );
}
