import './Products.css';
import Section from '../Section/Section';
import getAllProducts from '../../api/products/product.api';
import { useState, useEffect } from 'react';

export default function Products(props) {
  const [data, setData] = useState([]);

    useEffect(() => {
        getAllProducts().then((data) => {
            if (data.status) {
                console.log(data.result);
            }
        });
    }, []);

    return (
        <div>
            <h2>Продукты</h2>
            <div className="Products">
                {props.data.map((elem) => <Section name={elem.name} key={elem.id} />)}
            </div>
        </div>
    );
}
