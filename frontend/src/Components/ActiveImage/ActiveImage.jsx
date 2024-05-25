import './ActiveImage.css';
// import { useState, useEffect } from 'react';

export default function ActiveImage(props) {

    // const [file, setFile] = useState(null);
    // const [previewUrl, setPreviewUrl] = useState(null);

    // useEffect(() => {
    //     console.log(file);
    //     if (!file) {
    //       return;
    //     }
    
    //     setPreviewUrl(URL.createObjectURL(`http://localhost:8000/product_images/${props.data.uuid}.jpg`));
    //   }, [file]);

    return (
        <img 
            className="ActiveImage"
            src={`http://localhost:8000/product_images/${props.data ? props.data.uuid : 'trololo'}.jpg`}
        />
    );
}
