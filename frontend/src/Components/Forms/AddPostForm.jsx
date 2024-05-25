import './AddPostForm.css';
import { useSelector, useDispatch } from 'react-redux';
import { useState } from 'react';
import { createPost } from '../../api/posts/post.api';

export default function AddPostForm(props) {

    const addPostMenuState = useSelector((state) => state.addPostMenuState);
    const style = {display: addPostMenuState ? 'flex' : 'none'};
    const [selectedSubject, setSelectedSubject] = useState([]);
    const [selectedProductId, setSelectedProductId] = useState('');
    const [text, setText] = useState('');
    

    const selectSubjectHandle = (e) => {
        const [subject] = props.data.filter((subject) => subject.id == e.target.value);
        setSelectedSubject(subject || {})
    }

    const selectProductHandle = (e) => {
        setSelectedProductId(e.target.value);
    }

    const inputHandle = (e) => {
        setText(e.target.value);
    }

    const inputSubmit = (e) => {
        console.log(selectedProductId);
        console.log(text);
        createPost(selectedProductId, text).then((data) =>{
            console.log(data);
        });
        e.preventDefault();
    }

    return (
        <form className="AddPostForm" style={style} onSubmit={inputSubmit}>
            <div className='FormSide'>
                <div>Категории продуктов:</div>
                <select className='FormSelect' required onInput={selectSubjectHandle}>
                    <option value={''}>Выберете...</option>
                    {props.data.map(
                        (subject) => <option key={subject.id} value={subject.id}>
                                {subject.name}
                            </option>)
                    }
                </select>
                <div>Продукты:</div>
                <select className='FormSelect' required disabled={!selectedSubject.products} onInput={selectProductHandle}>
                    <option value={''}>Выберете...</option>
                    {selectedSubject.products && selectedSubject.products.map(
                        (product) => <option key={product.id} value={product.id}>
                                        {product.name}
                                    </option>)}
                </select>
                <button className={'Button'} type="submit" >Формировать пост</button>
            </div>
            <div className='FormSide'>
                <div >Текстовое описание:</div>
                <textarea required className='FormText' onInput={inputHandle}></textarea>
            </div>
        </form>
    );
}

// disabled={!selectedProductId}