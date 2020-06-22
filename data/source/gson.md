# File: `JsonTreeReader.java`

## Class: `JsonTreeReader`

        <!-- META {"entityType": "Class", "entitySignature": "JsonTreeReader", "entityFile": "JsonTreeReader.java"} -->This reader walks the elements of a JsonElement as if it was coming from a
        character stream.
        @author Jesse Wilson

# File: `JsonArray.java`

## Method: `public JsonArray()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonArray()", "entityFile": "JsonArray.java"} -->Creates an empty JsonArray.

# File: `TypeToken.java`

## Method: `protected TypeToken()`

        <!-- META {"entityType": "Method", "entitySignature": "protected TypeToken()", "entityFile": "TypeToken.java"} -->Constructs a new type literal. Derives represented class from type
        parameter.
        <p>Clients create an empty anonymous subclass. Doing so embeds the type
        parameter in the anonymous class's type hierarchy so we can reconstitute it
        at runtime despite erasure.

## Method: `TypeToken(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "TypeToken(Type type)", "entityFile": "TypeToken.java"} -->Unsafe. Constructs a type literal manually.

## Method: `static Type getSuperclassTypeParameter(Class<?> subclass)`

        <!-- META {"entityType": "Method", "entitySignature": "static Type getSuperclassTypeParameter(Class<?> subclass)", "entityFile": "TypeToken.java"} -->Returns the type from super class's type parameter in {@link $Gson$Types#canonicalize
        canonical form}.

## Method: `public final Class<? super T> getRawType()`

        <!-- META {"entityType": "Method", "entitySignature": "public final Class<? super T> getRawType()", "entityFile": "TypeToken.java"} -->Returns the raw (non-generic) type for this type.

# File: `JsonArray.java`

## Method: `public void add(Boolean bool)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(Boolean bool)", "entityFile": "JsonArray.java"} -->Adds the specified boolean to self.
        @param bool the boolean that needs to be added to the array.

# File: `FieldAttributes.java`

## Method: `public FieldAttributes(Field f)`

        <!-- META {"entityType": "Method", "entitySignature": "public FieldAttributes(Field f)", "entityFile": "FieldAttributes.java"} -->Constructs a Field Attributes object from the {@code f}.
        @param f the field to pull attributes from

# File: `TypeToken.java`

## Method: `public final Type getType()`

        <!-- META {"entityType": "Method", "entitySignature": "public final Type getType()", "entityFile": "TypeToken.java"} -->Gets underlying {@code Type} instance.

## Method: `public boolean isAssignableFrom(Class<?> cls)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isAssignableFrom(Class<?> cls)", "entityFile": "TypeToken.java"} -->Check if this type is assignable from the given class object.
        @deprecated this implementation may be inconsistent with javac for types
        with wildcards.

# File: `JsonTreeWriter.java`

## Field: `SENTINEL_CLOSED`

        <!-- META {"entityType": "Field", "entitySignature": "SENTINEL_CLOSED", "entityFile": "JsonTreeWriter.java"} -->Added to the top of the stack when this writer is closed to cause following ops to fail.

## Field: `stack`

        <!-- META {"entityType": "Field", "entitySignature": "stack", "entityFile": "JsonTreeWriter.java"} -->The JsonElements and JsonArrays under modification, outermost to innermost.

## Field: `pendingName`

        <!-- META {"entityType": "Field", "entitySignature": "pendingName", "entityFile": "JsonTreeWriter.java"} -->The name for the next JSON object value. If non-null, the top of the stack is a JsonObject.

## Method: `public JsonElement get()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement get()", "entityFile": "JsonTreeWriter.java"} -->Returns the top level object produced by this writer.

## Class: `JsonTreeWriter`

        <!-- META {"entityType": "Class", "entitySignature": "JsonTreeWriter", "entityFile": "JsonTreeWriter.java"} -->This writer creates a JsonElement.

# File: `TypeToken.java`

## Method: `public boolean isAssignableFrom(Type from)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isAssignableFrom(Type from)", "entityFile": "TypeToken.java"} -->Check if this type is assignable from the given Type.
        @deprecated this implementation may be inconsistent with javac for types
        with wildcards.

# File: `FieldAttributes.java`

## Method: `public Class<?> getDeclaringClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?> getDeclaringClass()", "entityFile": "FieldAttributes.java"} -->@return the declaring class that contains this field

## Method: `public String getName()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getName()", "entityFile": "FieldAttributes.java"} -->@return the name of the field

# File: `JsonArray.java`

## Method: `public void add(Character character)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(Character character)", "entityFile": "JsonArray.java"} -->Adds the specified character to self.
        @param character the character that needs to be added to the array.

# File: `FieldAttributes.java`

## Method: `public Type getDeclaredType()`

        <!-- META {"entityType": "Method", "entitySignature": "public Type getDeclaredType()", "entityFile": "FieldAttributes.java"} --><p>For example, assume the following class definition:
        <pre class="code">
        public class Foo {
        private String bar;
        private List&lt;String&gt; red;
        }
        Type listParameterizedType = new TypeToken&lt;List&lt;String&gt;&gt;() {}.getType();
        </pre>
        <p>This method would return {@code String.class} for the {@code bar} field and
        {@code listParameterizedType} for the {@code red} field.
        @return the specific type declared for this field

## Method: `public Class<?> getDeclaredClass()`

        <!-- META {"entityType": "Method", "entitySignature": "public Class<?> getDeclaredClass()", "entityFile": "FieldAttributes.java"} -->Returns the {@code Class} object that was declared for this field.
        <p>For example, assume the following class definition:
        <pre class="code">
        public class Foo {
        private String bar;
        private List&lt;String&gt; red;
        }
        </pre>
        <p>This method would return {@code String.class} for the {@code bar} field and
        {@code List.class} for the {@code red} field.
        @return the specific class object that was declared for the field

## Method: `public T getAnnotation(Class<T> annotation)`

        <!-- META {"entityType": "Method", "entitySignature": "public T getAnnotation(Class<T> annotation)", "entityFile": "FieldAttributes.java"} -->Return the {@code T} annotation object from this field if it exist; otherwise returns
        {@code null}.
        @param annotation the class of the annotation that will be retrieved
        @return the annotation instance if it is bound to the field; otherwise {@code null}

## Method: `public Collection<Annotation> getAnnotations()`

        <!-- META {"entityType": "Method", "entitySignature": "public Collection<Annotation> getAnnotations()", "entityFile": "FieldAttributes.java"} -->Return the annotations that are present on this field.
        @return an array of all the annotations set on the field
        @since 1.4

# File: `JsonArray.java`

## Method: `public void add(Number number)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(Number number)", "entityFile": "JsonArray.java"} -->Adds the specified number to self.
        @param number the number that needs to be added to the array.

## Method: `public void add(String string)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(String string)", "entityFile": "JsonArray.java"} -->Adds the specified string to self.
        @param string the string that needs to be added to the array.

## Method: `public void add(JsonElement element)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(JsonElement element)", "entityFile": "JsonArray.java"} -->Adds the specified element to self.
        @param element the element that needs to be added to the array.

## Method: `public void addAll(JsonArray array)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addAll(JsonArray array)", "entityFile": "JsonArray.java"} -->Adds all the elements of the specified array to self.
        @param array the array whose elements need to be added to the array.

## Method: `public JsonElement set(int index, JsonElement element)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement set(int index, JsonElement element)", "entityFile": "JsonArray.java"} -->Replaces the element at the specified position in this array with the specified element.
        Element can be null.
        @param index index of the element to replace
        @param element element to be stored at the specified position
        @return the element previously at the specified position
        @throws IndexOutOfBoundsException if the specified index is outside the array bounds

## Method: `public boolean remove(JsonElement element)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean remove(JsonElement element)", "entityFile": "JsonArray.java"} -->Removes the first occurrence of the specified element from this array, if it is present.
        If the array does not contain the element, it is unchanged.
        @param element element to be removed from this array, if present
        @return true if this array contained the specified element, false otherwise
        @since 2.3

## Method: `public JsonElement remove(int index)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement remove(int index)", "entityFile": "JsonArray.java"} -->Removes the element at the specified position in this array. Shifts any subsequent elements
        to the left (subtracts one from their indices). Returns the element that was removed from
        the array.
        @param index index the index of the element to be removed
        @return the element previously at the specified position
        @throws IndexOutOfBoundsException if the specified index is outside the array bounds
        @since 2.3

## Method: `public boolean contains(JsonElement element)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean contains(JsonElement element)", "entityFile": "JsonArray.java"} -->Returns true if this array contains the specified element.
        @return true if this array contains the specified element.
        @param element whose presence in this array is to be tested
        @since 2.3

## Method: `public int size()`

        <!-- META {"entityType": "Method", "entitySignature": "public int size()", "entityFile": "JsonArray.java"} -->Returns the number of elements in the array.
        @return the number of elements in the array.

## Method: `public Iterator<JsonElement> iterator()`

        <!-- META {"entityType": "Method", "entitySignature": "public Iterator<JsonElement> iterator()", "entityFile": "JsonArray.java"} -->Returns an iterator to navigate the elements of the array. Since the array is an ordered list,
        the iterator navigates the elements in the order they were inserted.
        @return an iterator to navigate the elements of the array.

## Method: `public JsonElement get(int i)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement get(int i)", "entityFile": "JsonArray.java"} -->Returns the ith element of the array.
        @param i the index of the element that is being sought.
        @return the element present at the ith index.
        @throws IndexOutOfBoundsException if i is negative or greater than or equal to the
        {@link #size()} of the array.

## Method: `public Number getAsNumber()`

        <!-- META {"entityType": "Method", "entitySignature": "public Number getAsNumber()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a {@link Number} if it contains a single element.
        @return get this element as a number if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid Number.
        @throws IllegalStateException if the array has more than one element.()<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public String getAsString()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getAsString()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a {@link String} if it contains a single element.
        @return get this element as a String if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid String.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public double getAsDouble()`

        <!-- META {"entityType": "Method", "entitySignature": "public double getAsDouble()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a double if it contains a single element.
        @return get this element as a double if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid double.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public BigDecimal getAsBigDecimal()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigDecimal getAsBigDecimal()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a {@link BigDecimal} if it contains a single element.
        @return get this element as a {@link BigDecimal} if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive}.
        @throws NumberFormatException if the element at index 0 is not a valid {@link BigDecimal}.
        @throws IllegalStateException if the array has more than one element.
        @since 1.2<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public BigInteger getAsBigInteger()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigInteger getAsBigInteger()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a {@link BigInteger} if it contains a single element.
        @return get this element as a {@link BigInteger} if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive}.
        @throws NumberFormatException if the element at index 0 is not a valid {@link BigInteger}.
        @throws IllegalStateException if the array has more than one element.
        @since 1.2<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public float getAsFloat()`

        <!-- META {"entityType": "Method", "entitySignature": "public float getAsFloat()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a float if it contains a single element.
        @return get this element as a float if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid float.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public long getAsLong()`

        <!-- META {"entityType": "Method", "entitySignature": "public long getAsLong()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a long if it contains a single element.
        @return get this element as a long if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid long.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public int getAsInt()`

        <!-- META {"entityType": "Method", "entitySignature": "public int getAsInt()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as an integer if it contains a single element.
        @return get this element as an integer if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid integer.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

# File: `FieldAttributes.java`

## Method: `public boolean hasModifier(int modifier)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasModifier(int modifier)", "entityFile": "FieldAttributes.java"} -->Returns {@code true} if the field is defined with the {@code modifier}.
        <p>This method is meant to be called as:
        <pre class="code">
        boolean hasPublicModifier = fieldAttribute.hasModifier(java.lang.reflect.Modifier.PUBLIC);
        </pre>
        @see java.lang.reflect.Modifier

## Method: `Object get(Object instance) throws IllegalAccessException`

        <!-- META {"entityType": "Method", "entitySignature": "Object get(Object instance) throws IllegalAccessException", "entityFile": "FieldAttributes.java"} -->This is exposed internally only for the removing synthetic fields from the JSON output.
        @return true if the field is synthetic; otherwise false
        @throws IllegalAccessException
        @throws IllegalArgumentException

## Method: `boolean isSynthetic()`

        <!-- META {"entityType": "Method", "entitySignature": "boolean isSynthetic()", "entityFile": "FieldAttributes.java"} -->This is exposed internally only for the removing synthetic fields from the JSON output.
        @return true if the field is synthetic; otherwise false

## Class: `FieldAttributes`

        <!-- META {"entityType": "Class", "entitySignature": "FieldAttributes", "entityFile": "FieldAttributes.java"} -->A data object that stores attributes of a field.
        <p>This class is immutable; therefore, it can be safely shared across threads.
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.4

# File: `JsonArray.java`

## Method: `public short getAsShort()`

        <!-- META {"entityType": "Method", "entitySignature": "public short getAsShort()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a primitive short if it contains a single element.
        @return get this element as a primitive short if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid short.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Method: `public boolean getAsBoolean()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean getAsBoolean()", "entityFile": "JsonArray.java"} --><!-- 99ceab2c-1733-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this array as a boolean if it contains a single element.
        @return get this element as a boolean if it is single element array.
        @throws ClassCastException if the element in the array is of not a {@link JsonPrimitive} and
        is not a valid boolean.
        @throws IllegalStateException if the array has more than one element.<!-- ACCEPT >=> 99ceab2c-1733-11ea-afaf-333445793454 -->

## Class: `JsonArray`

        <!-- META {"entityType": "Class", "entitySignature": "JsonArray", "entityFile": "JsonArray.java"} -->A class representing an array type in Json. An array is a list of {@link JsonElement}s each of
        which can be of a different type. This is an ordered list, meaning that the order in which
        elements are added is preserved.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TypeToken.java`

## Method: `public boolean isAssignableFrom(TypeToken<?> token)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isAssignableFrom(TypeToken<?> token)", "entityFile": "TypeToken.java"} -->Check if this type is assignable from the given type token.
        @deprecated this implementation may be inconsistent with javac for types
        with wildcards.

## Method: `private static boolean isAssignableFrom(Type from, GenericArrayType to)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean isAssignableFrom(Type from, GenericArrayType to)", "entityFile": "TypeToken.java"} -->Private helper function that performs some assignability checks for
        the provided GenericArrayType.

## Method: `private static boolean isAssignableFrom(Type from, ParameterizedType to, Map<String, Type> typeVarMap)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean isAssignableFrom(Type from, ParameterizedType to, Map<String, Type> typeVarMap)", "entityFile": "TypeToken.java"} -->Private recursive helper function to actually do the type-safe checking
        of assignability.

## Method: `private static boolean typeEquals(ParameterizedType from, ParameterizedType to, Map<String, Type> typeVarMap)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean typeEquals(ParameterizedType from, ParameterizedType to, Map<String, Type> typeVarMap)", "entityFile": "TypeToken.java"} -->Checks if two parameterized types are exactly equal, under the variable
        replacement described in the typeVarMap.

## Method: `private static boolean matches(Type from, Type to, Map<String, Type> typeMap)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean matches(Type from, Type to, Map<String, Type> typeMap)", "entityFile": "TypeToken.java"} -->Checks if two types are the same or are equivalent under a variable mapping
        given in the type map that was provided.

## Method: `public static TypeToken<?> get(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeToken<?> get(Type type)", "entityFile": "TypeToken.java"} -->Gets type literal for the given {@code Type} instance.

## Method: `public static TypeToken<T> get(Class<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeToken<T> get(Class<T> type)", "entityFile": "TypeToken.java"} -->Gets type literal for the given {@code Class} instance.

## Class: `TypeToken`

        <!-- META {"entityType": "Class", "entitySignature": "TypeToken", "entityFile": "TypeToken.java"} -->Represents a generic type {@code T}. Java doesn't yet provide a way to
        represent generic types, so this class does. Forces clients to create a
        subclass of this class which enables retrieval the type information even at
        runtime.
        <p>For example, to create a type literal for {@code List<String>}, you can
        create an empty anonymous inner class:
        <p>
        {@code TypeToken<List<String>> list = new TypeToken<List<String>>() {};}
        <p>This syntax cannot be used to create type literals that have wildcard
        parameters, such as {@code Class<?>} or {@code List<? extends CharSequence>}.
        @author Bob Lee
        @author Sven Mawson
        @author Jesse Wilson

# File: `FieldNamingPolicy.java`

## EnumConstant: `IDENTITY`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "IDENTITY", "entityFile": "FieldNamingPolicy.java"} -->Using this naming policy with Gson will ensure that the field name is
        unchanged.

# File: `JsonDeserializationContext.java`

## Method: `public T deserialize(JsonElement json, Type typeOfT) throws JsonParseException`

        <!-- META {"entityType": "Method", "entitySignature": "public T deserialize(JsonElement json, Type typeOfT) throws JsonParseException", "entityFile": "JsonDeserializationContext.java"} -->Invokes default deserialization on the specified object. It should never be invoked on
        the element received as a parameter of the
        {@link JsonDeserializer#deserialize(JsonElement, Type, JsonDeserializationContext)} method. Doing
        so will result in an infinite loop since Gson will in-turn call the custom deserializer again.
        @param json the parse tree.
        @param typeOfT type of the expected return value.
        @param <T> The type of the deserialized object.
        @return An object of type typeOfT.
        @throws JsonParseException if the parse tree does not contain expected data.

## Interface: `JsonDeserializationContext`

        <!-- META {"entityType": "Interface", "entitySignature": "JsonDeserializationContext", "entityFile": "JsonDeserializationContext.java"} -->Context for deserialization that is passed to a custom deserializer during invocation of its
        {@link JsonDeserializer#deserialize(JsonElement, Type, JsonDeserializationContext)}
        method.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `JsonDeserializer.java`

## Method: `public T deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException`

        <!-- META {"entityType": "Method", "entitySignature": "public T deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws JsonParseException", "entityFile": "JsonDeserializer.java"} -->Gson invokes this call-back method during deserialization when it encounters a field of the
        specified type.
        <p>In the implementation of this call-back method, you should consider invoking
        {@link JsonDeserializationContext#deserialize(JsonElement, Type)} method to create objects
        for any non-trivial field of the returned object. However, you should never invoke it on the
        the same type passing {@code json} since that will cause an infinite loop (Gson will call your
        call-back method again).
        @param json The Json data being deserialized
        @param typeOfT The type of the Object to deserialize to
        @return a deserialized object of the specified type typeOfT which is a subclass of {@code T}
        @throws JsonParseException if json is not in the expected format of {@code typeofT}

# File: `MapTypeAdapterFactory.java`

## Method: `private TypeAdapter<?> getKeyAdapter(Gson context, Type keyType)`

        <!-- META {"entityType": "Method", "entitySignature": "private TypeAdapter<?> getKeyAdapter(Gson context, Type keyType)", "entityFile": "MapTypeAdapterFactory.java"} -->Returns a type adapter that writes the value as a string.

# File: `FieldNamingPolicy.java`

## EnumConstant: `UPPER_CAMEL_CASE`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "UPPER_CAMEL_CASE", "entityFile": "FieldNamingPolicy.java"} -->Using this naming policy with Gson will ensure that the first "letter" of the Java
        field name is capitalized when serialized to its JSON form.
        <p>Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":</p>
        <ul>
        <li>someFieldName ---> SomeFieldName</li>
        <li>_someFieldName ---> _SomeFieldName</li>
        </ul>

# File: `JsonDeserializer.java`

## Interface: `JsonDeserializer`

        <!-- META {"entityType": "Interface", "entitySignature": "JsonDeserializer", "entityFile": "JsonDeserializer.java"} --><p>Interface representing a custom deserializer for Json. You should write a custom
        deserializer, if you are not happy with the default deserialization done by Gson. You will
        also need to register this deserializer through
        {@link GsonBuilder#registerTypeAdapter(Type, Object)}.</p>
        <p>Let us look at example where defining a deserializer will be useful. The {@code Id} class
        defined below has two fields: {@code clazz} and {@code value}.</p>
        <pre>
        public class Id&lt;T&gt; {
        private final Class&lt;T&gt; clazz;
        private final long value;
        public Id(Class&lt;T&gt; clazz, long value) {
        this.clazz = clazz;
        this.value = value;
        }
        public long getValue() {
        return value;
        }
        }
        </pre>
        <p>The default deserialization of {@code Id(com.foo.MyObject.class, 20L)} will require the
        Json string to be <code>{"clazz":com.foo.MyObject,"value":20}</code>. Suppose, you already know
        the type of the field that the {@code Id} will be deserialized into, and hence just want to
        deserialize it from a Json string {@code 20}. You can achieve that by writing a custom
        deserializer:</p>
        <pre>
        class IdDeserializer implements JsonDeserializer&lt;Id&gt;() {
        public Id deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context)
        throws JsonParseException {
        return new Id((Class)typeOfT, id.getValue());
        }
        </pre>
        <p>You will also need to register {@code IdDeserializer} with Gson as follows:</p>
        <pre>
        Gson gson = new GsonBuilder().registerTypeAdapter(Id.class, new IdDeserializer()).create();
        </pre>
        <p>New applications should prefer {@link TypeAdapter}, whose streaming API
        is more efficient than this interface's tree API.
        @author Inderjeet Singh
        @author Joel Leitch
        @param <T> type for which the deserializer is being registered. It is possible that a
        deserializer may be asked to deserialize a specific generic type of the T.

# File: `FieldNamingPolicy.java`

## EnumConstant: `UPPER_CAMEL_CASE_WITH_SPACES`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "UPPER_CAMEL_CASE_WITH_SPACES", "entityFile": "FieldNamingPolicy.java"} -->Using this naming policy with Gson will ensure that the first "letter" of the Java
        field name is capitalized when serialized to its JSON form and the words will be
        separated by a space.
        <p>Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":</p>
        <ul>
        <li>someFieldName ---> Some Field Name</li>
        <li>_someFieldName ---> _Some Field Name</li>
        </ul>
        @since 1.4

## EnumConstant: `LOWER_CASE_WITH_UNDERSCORES`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "LOWER_CASE_WITH_UNDERSCORES", "entityFile": "FieldNamingPolicy.java"} -->Using this naming policy with Gson will modify the Java Field name from its camel cased
        form to a lower case field name where each word is separated by an underscore (_).
        <p>Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":</p>
        <ul>
        <li>someFieldName ---> some_field_name</li>
        <li>_someFieldName ---> _some_field_name</li>
        <li>aStringField ---> a_string_field</li>
        <li>aURL ---> a_u_r_l</li>
        </ul>

## EnumConstant: `LOWER_CASE_WITH_DASHES`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "LOWER_CASE_WITH_DASHES", "entityFile": "FieldNamingPolicy.java"} -->Using this naming policy with Gson will modify the Java Field name from its camel cased
        form to a lower case field name where each word is separated by a dash (-).
        <p>Here's a few examples of the form "Java Field Name" ---> "JSON Field Name":</p>
        <ul>
        <li>someFieldName ---> some-field-name</li>
        <li>_someFieldName ---> _some-field-name</li>
        <li>aStringField ---> a-string-field</li>
        <li>aURL ---> a-u-r-l</li>
        </ul>
        Using dashes in JavaScript is not recommended since dash is also used for a minus sign in
        expressions. This requires that a field named with dashes is always accessed as a quoted
        property like {@code myobject['my-field']}. Accessing it as an object field
        {@code myobject.my-field} will result in an unintended javascript expression.
        @since 1.4

## Method: `static String separateCamelCase(String name, String separator)`

        <!-- META {"entityType": "Method", "entitySignature": "static String separateCamelCase(String name, String separator)", "entityFile": "FieldNamingPolicy.java"} -->Converts the field name that uses camel-case define word separation into
        separate words that are separated by the provided {@code separatorString}.

## Method: `static String upperCaseFirstLetter(String name)`

        <!-- META {"entityType": "Method", "entitySignature": "static String upperCaseFirstLetter(String name)", "entityFile": "FieldNamingPolicy.java"} -->Ensures the JSON field names begins with an upper case letter.

## Enum: `FieldNamingPolicy`

        <!-- META {"entityType": "Enum", "entitySignature": "FieldNamingPolicy", "entityFile": "FieldNamingPolicy.java"} -->An enumeration that defines a few standard naming conventions for JSON field names.
        This enumeration should be used in conjunction with {@link com.google.gson.GsonBuilder}
        to configure a {@link com.google.gson.Gson} instance to properly translate Java field
        names into the desired JSON field names.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `FieldNamingStrategy.java`

## Method: `public String translateName(Field f)`

        <!-- META {"entityType": "Method", "entitySignature": "public String translateName(Field f)", "entityFile": "FieldNamingStrategy.java"} -->Translates the field name into its JSON field name representation.
        @param f the field object that we are translating
        @return the translated field name.
        @since 1.3

## Interface: `FieldNamingStrategy`

        <!-- META {"entityType": "Interface", "entitySignature": "FieldNamingStrategy", "entityFile": "FieldNamingStrategy.java"} -->A mechanism for providing custom field naming in Gson.  This allows the client code to translate
        field names into a particular convention that is not supported as a normal Java field
        declaration rules.  For example, Java does not support "-" characters in a field name.
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.3

# File: `MapTypeAdapterFactory.java`

## Class: `MapTypeAdapterFactory`

        <!-- META {"entityType": "Class", "entitySignature": "MapTypeAdapterFactory", "entityFile": "MapTypeAdapterFactory.java"} -->Adapts maps to either JSON objects or JSON arrays.
        <h3>Maps as JSON objects</h3>
        For primitive keys or when complex map key serialization is not enabled, this
        converts Java {@link Map Maps} to JSON Objects. This requires that map keys
        can be serialized as strings; this is insufficient for some key types. For
        example, consider a map whose keys are points on a grid. The default JSON
        form encodes reasonably: <pre>   {@code
        Map<Point, String> original = new LinkedHashMap<Point, String>();
        original.put(new Point(5, 6), "a");
        original.put(new Point(8, 8), "b");
        System.out.println(gson.toJson(original, type));
        }</pre>
        The above code prints this JSON object:<pre>   {@code
        {
        "(5,6)": "a",
        "(8,8)": "b"
        }
        }</pre>
        But GSON is unable to deserialize this value because the JSON string name is
        just the {@link Object#toString() toString()} of the map key. Attempting to
        convert the above JSON to an object fails with a parse exception:
        <pre>com.google.gson.JsonParseException: Expecting object found: "(5,6)"
        at com.google.gson.JsonObjectDeserializationVisitor.visitFieldUsingCustomHandler
        at com.google.gson.ObjectNavigator.navigateClassFields
        ...</pre>
        <h3>Maps as JSON arrays</h3>
        An alternative approach taken by this type adapter when it is required and
        complex map key serialization is enabled is to encode maps as arrays of map
        entries. Each map entry is a two element array containing a key and a value.
        This approach is more flexible because any type can be used as the map's key;
        not just strings. But it's also less portable because the receiver of such
        JSON must be aware of the map entry convention.
        <p>Register this adapter when you are creating your GSON instance.
        <pre>   {@code
        Gson gson = new GsonBuilder()
        .registerTypeAdapter(Map.class, new MapAsArrayTypeAdapter())
        .create();
        }</pre>
        This will change the structure of the JSON emitted by the code above. Now we
        get an array. In this case the arrays elements are map entries:
        <pre>   {@code
        [
        [
        {
        "x": 5,
        "y": 6
        },
        "a",
        ],
        [
        {
        "x": 8,
        "y": 8
        },
        "b"
        ]
        ]
        }</pre>
        This format will serialize and deserialize just fine as long as this adapter
        is registered.

# File: `JsonElement.java`

## Method: `abstract JsonElement deepCopy()`

        <!-- META {"entityType": "Method", "entitySignature": "abstract JsonElement deepCopy()", "entityFile": "JsonElement.java"} -->Returns a deep copy of this element. Immutable elements like primitives
        and nulls are not copied.

## Method: `public boolean isJsonArray()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isJsonArray()", "entityFile": "JsonElement.java"} -->provides check for verifying if this element is an array or not.
        @return true if this element is of type {@link JsonArray}, false otherwise.

## Method: `public boolean isJsonObject()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isJsonObject()", "entityFile": "JsonElement.java"} -->provides check for verifying if this element is a Json object or not.
        @return true if this element is of type {@link JsonObject}, false otherwise.

## Method: `public boolean isJsonPrimitive()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isJsonPrimitive()", "entityFile": "JsonElement.java"} -->provides check for verifying if this element is a primitive or not.
        @return true if this element is of type {@link JsonPrimitive}, false otherwise.

## Method: `public boolean isJsonNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isJsonNull()", "entityFile": "JsonElement.java"} -->provides check for verifying if this element represents a null value or not.
        @return true if this element is of type {@link JsonNull}, false otherwise.
        @since 1.2

## Method: `public JsonObject getAsJsonObject()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonObject getAsJsonObject()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1738-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link JsonObject}. If the element is of some
        other type, a {@link IllegalStateException} will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling {@link #isJsonObject()}
        first.
        @return get this element as a {@link JsonObject}.
        @throws IllegalStateException if the element is of another type.<!-- ACCEPT >=> 99ceab2c-1738-11ea-afaf-333445793454 -->

## Method: `public JsonArray getAsJsonArray()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonArray getAsJsonArray()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1738-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link JsonArray}. If the element is of some
        other type, a {@link IllegalStateException} will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling {@link #isJsonArray()}
        first.
        @return get this element as a {@link JsonArray}.
        @throws IllegalStateException if the element is of another type.<!-- ACCEPT >=> 99ceab2c-1738-11ea-afaf-333445793454 -->

## Method: `public JsonPrimitive getAsJsonPrimitive()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive getAsJsonPrimitive()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1738-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link JsonPrimitive}. If the element is of some
        other type, a {@link IllegalStateException} will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling {@link #isJsonPrimitive()}
        first.
        @return get this element as a {@link JsonPrimitive}.
        @throws IllegalStateException if the element is of another type.<!-- ACCEPT >=> 99ceab2c-1738-11ea-afaf-333445793454 -->

## Method: `public JsonNull getAsJsonNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonNull getAsJsonNull()", "entityFile": "JsonElement.java"} -->convenience method to get this element as a {@link JsonNull}. If the element is of some
        other type, a {@link IllegalStateException} will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling {@link #isJsonNull()}
        first.
        @return get this element as a {@link JsonNull}.
        @throws IllegalStateException if the element is of another type.
        @since 1.2

## Method: `public boolean getAsBoolean()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean getAsBoolean()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a boolean value.
        @return get this element as a primitive boolean value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        boolean value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `Boolean getAsBooleanWrapper()`

        <!-- META {"entityType": "Method", "entitySignature": "Boolean getAsBooleanWrapper()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link Boolean} value.
        @return get this element as a {@link Boolean} value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        boolean value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.
        <!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public Number getAsNumber()`

        <!-- META {"entityType": "Method", "entitySignature": "public Number getAsNumber()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link Number}.
        @return get this element as a {@link Number}.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        number.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

# File: `ObjectTypeAdapter.java`

## Class: `ObjectTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "ObjectTypeAdapter", "entityFile": "ObjectTypeAdapter.java"} -->Adapts types whose static type is only 'Object'. Uses getClass() on
        serialization and a primitive/Map/List on deserialization.

# File: `ArrayTypeAdapter.java`

## Class: `ArrayTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "ArrayTypeAdapter", "entityFile": "ArrayTypeAdapter.java"} -->Adapt an array of objects.

# File: `JsonElement.java`

## Method: `public String getAsString()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getAsString()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a string value.
        @return get this element as a string value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        string value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public double getAsDouble()`

        <!-- META {"entityType": "Method", "entitySignature": "public double getAsDouble()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive double value.
        @return get this element as a primitive double value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        double value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public float getAsFloat()`

        <!-- META {"entityType": "Method", "entitySignature": "public float getAsFloat()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive float value.
        @return get this element as a primitive float value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        float value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public long getAsLong()`

        <!-- META {"entityType": "Method", "entitySignature": "public long getAsLong()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive long value.
        @return get this element as a primitive long value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        long value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public int getAsInt()`

        <!-- META {"entityType": "Method", "entitySignature": "public int getAsInt()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive integer value.
        @return get this element as a primitive integer value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        integer value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public byte getAsByte()`

        <!-- META {"entityType": "Method", "entitySignature": "public byte getAsByte()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive byte value.
        @return get this element as a primitive byte value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        byte value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.
        @since 1.3<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public char getAsCharacter()`

        <!-- META {"entityType": "Method", "entitySignature": "public char getAsCharacter()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1736-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive character value.
        @return get this element as a primitive char value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        char value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.
        @since 1.3<!-- ACCEPT >=> 99ceab2c-1736-11ea-afaf-333445793454 -->

## Method: `public BigDecimal getAsBigDecimal()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigDecimal getAsBigDecimal()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1735-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link BigDecimal}.
        @return get this element as a {@link BigDecimal}.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive}.
        * @throws NumberFormatException if the element is not a valid {@link BigDecimal}.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.
        @since 1.2<!-- ACCEPT >=> 99ceab2c-1735-11ea-afaf-333445793454 -->

## Method: `public BigInteger getAsBigInteger()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigInteger getAsBigInteger()", "entityFile": "JsonElement.java"} --><!-- 99ceab2c-1735-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link BigInteger}.
        @return get this element as a {@link BigInteger}.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive}.
        @throws NumberFormatException if the element is not a valid {@link BigInteger}.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.
        @since 1.2<!-- ACCEPT >=> 99ceab2c-1735-11ea-afaf-333445793454 -->

## Method: `public short getAsShort()`

        <!-- META {"entityType": "Method", "entitySignature": "public short getAsShort()", "entityFile": "JsonElement.java"} -->convenience method to get this element as a primitive short value.
        @return get this element as a primitive short value.
        @throws ClassCastException if the element is of not a {@link JsonPrimitive} and is not a valid
        short value.
        @throws IllegalStateException if the element is of the type {@link JsonArray} but contains
        more than a single element.

## Method: `public String toString()`

        <!-- META {"entityType": "Method", "entitySignature": "public String toString()", "entityFile": "JsonElement.java"} -->Returns a String representation of this element.

## Class: `JsonElement`

        <!-- META {"entityType": "Class", "entitySignature": "JsonElement", "entityFile": "JsonElement.java"} -->A class representing an element of Json. It could either be a {@link JsonObject}, a
        {@link JsonArray}, a {@link JsonPrimitive} or a {@link JsonNull}.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `JsonIOException.java`

## Method: `public JsonIOException(Throwable cause)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonIOException(Throwable cause)", "entityFile": "JsonIOException.java"} -->Creates exception with the specified cause. Consider using
        {@link #JsonIOException(String, Throwable)} instead if you can describe what happened.
        @param cause root exception that caused this exception to be thrown.

## Class: `JsonIOException`

        <!-- META {"entityType": "Class", "entitySignature": "JsonIOException", "entityFile": "JsonIOException.java"} -->This exception is raised when Gson was unable to read an input stream
        or write to one.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `CollectionTypeAdapterFactory.java`

## Class: `CollectionTypeAdapterFactory`

        <!-- META {"entityType": "Class", "entitySignature": "CollectionTypeAdapterFactory", "entityFile": "CollectionTypeAdapterFactory.java"} -->Adapt a homogeneous collection of objects.

# File: `DateTypeAdapter.java`

## Class: `DateTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "DateTypeAdapter", "entityFile": "DateTypeAdapter.java"} --><!-- 737161d5-1740-11ea-b3f9-333445793454 <=< ACCEPT -->Adapter for Date. Although this class appears stateless, it is not.
        DateFormat captures its time zone and locale when it is created, which gives
        this class state. DateFormat isn't thread safe either, so this class has
        to synchronize its read and write methods.<!-- ACCEPT >=> 737161d5-1740-11ea-b3f9-333445793454 -->

# File: `JsonNull.java`

## Field: `INSTANCE`

        <!-- META {"entityType": "Field", "entitySignature": "INSTANCE", "entityFile": "JsonNull.java"} -->singleton for JsonNull
        @since 1.8

## Method: `public JsonNull()`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonNull()", "entityFile": "JsonNull.java"} -->Creates a new JsonNull object.
        Deprecated since Gson version 1.8. Use {@link #INSTANCE} instead

## Method: `public int hashCode()`

        <!-- META {"entityType": "Method", "entitySignature": "public int hashCode()", "entityFile": "JsonNull.java"} -->All instances of JsonNull have the same hash code since they are indistinguishable

## Method: `public boolean equals(Object other)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean equals(Object other)", "entityFile": "JsonNull.java"} -->All instances of JsonNull are the same

## Class: `JsonNull`

        <!-- META {"entityType": "Class", "entitySignature": "JsonNull", "entityFile": "JsonNull.java"} -->A class representing a Json {@code null} value.
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.2

# File: `JsonObject.java`

## Method: `public void add(String property, JsonElement value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void add(String property, JsonElement value)", "entityFile": "JsonObject.java"} -->Adds a member, which is a name-value pair, to self. The name must be a String, but the value
        can be an arbitrary JsonElement, thereby allowing you to build a full tree of JsonElements
        rooted at this node.
        @param property name of the member.
        @param value the member object.

## Method: `public JsonElement remove(String property)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement remove(String property)", "entityFile": "JsonObject.java"} -->Removes the {@code property} from this {@link JsonObject}.
        @param property name of the member that should be removed.
        @return the {@link JsonElement} object that is being removed.
        @since 1.3

## Method: `public void addProperty(String property, String value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addProperty(String property, String value)", "entityFile": "JsonObject.java"} -->Convenience method to add a primitive member. The specified value is converted to a
        JsonPrimitive of String.
        @param property name of the member.
        @param value the string value associated with the member.

## Method: `public void addProperty(String property, Number value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addProperty(String property, Number value)", "entityFile": "JsonObject.java"} -->Convenience method to add a primitive member. The specified value is converted to a
        JsonPrimitive of Number.
        @param property name of the member.
        @param value the number value associated with the member.

## Method: `public void addProperty(String property, Boolean value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addProperty(String property, Boolean value)", "entityFile": "JsonObject.java"} -->Convenience method to add a boolean member. The specified value is converted to a
        JsonPrimitive of Boolean.
        @param property name of the member.
        @param value the number value associated with the member.

## Method: `public void addProperty(String property, Character value)`

        <!-- META {"entityType": "Method", "entitySignature": "public void addProperty(String property, Character value)", "entityFile": "JsonObject.java"} -->Convenience method to add a char member. The specified value is converted to a
        JsonPrimitive of Character.
        @param property name of the member.
        @param value the number value associated with the member.

## Method: `private JsonElement createJsonElement(Object value)`

        <!-- META {"entityType": "Method", "entitySignature": "private JsonElement createJsonElement(Object value)", "entityFile": "JsonObject.java"} -->Creates the proper {@link JsonElement} object from the given {@code value} object.
        @param value the object to generate the {@link JsonElement} for
        @return a {@link JsonPrimitive} if the {@code value} is not null, otherwise a {@link JsonNull}

## Method: `public Set<Map.Entry<String, JsonElement>> entrySet()`

        <!-- META {"entityType": "Method", "entitySignature": "public Set<Map.Entry<String, JsonElement>> entrySet()", "entityFile": "JsonObject.java"} -->Returns a set of members of this object. The set is ordered, and the order is in which the
        elements were added.
        @return a set of members of this object.

## Method: `public boolean has(String memberName)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean has(String memberName)", "entityFile": "JsonObject.java"} -->Convenience method to check if a member with the specified name is present in this object.
        @param memberName name of the member that is being checked for presence.
        @return true if there is a member with the specified name, false otherwise.

## Method: `public JsonElement get(String memberName)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement get(String memberName)", "entityFile": "JsonObject.java"} -->Returns the member with the specified name.
        @param memberName name of the member that is being requested.
        @return the member matching the name. Null if no such member exists.

## Method: `public JsonPrimitive getAsJsonPrimitive(String memberName)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive getAsJsonPrimitive(String memberName)", "entityFile": "JsonObject.java"} --><!-- 92af53ff-1740-11ea-85cc-333445793454 <=< ACCEPT -->Convenience method to get the specified member as a JsonPrimitive element.
        @param memberName name of the member being requested.
        @return the JsonPrimitive corresponding to the specified member.<!-- ACCEPT >=> 92af53ff-1740-11ea-85cc-333445793454 -->

## Method: `public JsonArray getAsJsonArray(String memberName)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonArray getAsJsonArray(String memberName)", "entityFile": "JsonObject.java"} --><!-- 92af53ff-1740-11ea-85cc-333445793454 <=< ACCEPT -->Convenience method to get the specified member as a JsonArray.
        @param memberName name of the member being requested.
        @return the JsonArray corresponding to the specified member.<!-- ACCEPT >=> 92af53ff-1740-11ea-85cc-333445793454 -->

## Method: `public JsonObject getAsJsonObject(String memberName)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonObject getAsJsonObject(String memberName)", "entityFile": "JsonObject.java"} --><!-- 92af53ff-1740-11ea-85cc-333445793454 <=< ACCEPT -->Convenience method to get the specified member as a JsonObject.
        @param memberName name of the member being requested.
        @return the JsonObject corresponding to the specified member.<!-- ACCEPT >=> 92af53ff-1740-11ea-85cc-333445793454 -->

## Class: `JsonObject`

        <!-- META {"entityType": "Class", "entitySignature": "JsonObject", "entityFile": "JsonObject.java"} -->A class representing an object type in Json. An object consists of name-value pairs where names
        are strings, and values are any other type of {@link JsonElement}. This allows for a creating a
        tree of JsonElements. The member elements of this object are maintained in order they were added.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `Gson.java`

## Field: `calls`

        <!-- META {"entityType": "Field", "entitySignature": "calls", "entityFile": "Gson.java"} -->This thread local guards against reentrant calls to getAdapter(). In
        certain object graphs, creating an adapter for a type may recursively
        require an adapter for the same type! Without intervention, the recursive
        lookup would stack overflow. We cheat by returning a proxy type adapter.
        The proxy is wired up once the initial adapter has been created.

# File: `JsonAdapterAnnotationTypeAdapterFactory.java`

## Class: `JsonAdapterAnnotationTypeAdapterFactory`

        <!-- META {"entityType": "Class", "entitySignature": "JsonAdapterAnnotationTypeAdapterFactory", "entityFile": "JsonAdapterAnnotationTypeAdapterFactory.java"} -->Given a type T, looks for the annotation {@link JsonAdapter} and uses an instance of the
        specified class as the default type adapter.
        @since 2.3

# File: `Gson.java`

## Method: `public Gson()`

        <!-- META {"entityType": "Method", "entitySignature": "public Gson()", "entityFile": "Gson.java"} -->Constructs a Gson object with default configuration. The default configuration has the
        following settings:
        <ul>
        <li>The JSON generated by <code>toJson</code> methods is in compact representation. This
        means that all the unneeded white-space is removed. You can change this behavior with
        {@link GsonBuilder#setPrettyPrinting()}. </li>
        <li>The generated JSON omits all the fields that are null. Note that nulls in arrays are
        kept as is since an array is an ordered list. Moreover, if a field is not null, but its
        generated JSON is empty, the field is kept. You can configure Gson to serialize null values
        by setting {@link GsonBuilder#serializeNulls()}.</li>
        <li>Gson provides default serialization and deserialization for Enums, {@link Map},
        {@link java.net.URL}, {@link java.net.URI}, {@link java.util.Locale}, {@link java.util.Date},
        {@link java.math.BigDecimal}, and {@link java.math.BigInteger} classes. If you would prefer
        to change the default representation, you can do so by registering a type adapter through
        {@link GsonBuilder#registerTypeAdapter(Type, Object)}. </li>
        <li>The default Date format is same as {@link java.text.DateFormat#DEFAULT}. This format
        ignores the millisecond portion of the date during serialization. You can change
        this by invoking {@link GsonBuilder#setDateFormat(int)} or
        {@link GsonBuilder#setDateFormat(String)}. </li>
        <li>By default, Gson ignores the {@link com.google.gson.annotations.Expose} annotation.
        You can enable Gson to serialize/deserialize only those fields marked with this annotation
        through {@link GsonBuilder#excludeFieldsWithoutExposeAnnotation()}. </li>
        <li>By default, Gson ignores the {@link com.google.gson.annotations.Since} annotation. You
        can enable Gson to use this annotation through {@link GsonBuilder#setVersion(double)}.</li>
        <li>The default field naming policy for the output Json is same as in Java. So, a Java class
        field <code>versionNumber</code> will be output as <code>&quot;versionNumber&quot;</code> in
        Json. The same rules are applied for mapping incoming Json to the Java classes. You can
        change this policy through {@link GsonBuilder#setFieldNamingPolicy(FieldNamingPolicy)}.</li>
        <li>By default, Gson excludes <code>transient</code> or <code>static</code> fields from
        consideration for serialization and deserialization. You can change this behavior through
        {@link GsonBuilder#excludeFieldsWithModifiers(int...)}.</li>
        </ul>

# File: `JsonParseException.java`

## Method: `public JsonParseException(String msg)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonParseException(String msg)", "entityFile": "JsonParseException.java"} -->Creates exception with the specified message. If you are wrapping another exception, consider
        using {@link #JsonParseException(String, Throwable)} instead.
        @param msg error message describing a possible cause of this exception.

## Method: `public JsonParseException(String msg, Throwable cause)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonParseException(String msg, Throwable cause)", "entityFile": "JsonParseException.java"} -->Creates exception with the specified message and cause.
        @param msg error message describing what happened.
        @param cause root exception that caused this exception to be thrown.

## Method: `public JsonParseException(Throwable cause)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonParseException(Throwable cause)", "entityFile": "JsonParseException.java"} -->Creates exception with the specified cause. Consider using
        {@link #JsonParseException(String, Throwable)} instead if you can describe what happened.
        @param cause root exception that caused this exception to be thrown.

## Class: `JsonParseException`

        <!-- META {"entityType": "Class", "entitySignature": "JsonParseException", "entityFile": "JsonParseException.java"} -->This exception is raised if there is a serious issue that occurs during parsing of a Json
        string.  One of the main usages for this class is for the Gson infrastructure.  If the incoming
        Json is bad/malicious, an instance of this exception is raised.
        <p>This exception is a {@link RuntimeException} because it is exposed to the client.  Using a
        {@link RuntimeException} avoids bad coding practices on the client side where they catch the
        exception and do nothing.  It is often the case that you want to blow up if there is a parsing
        error (i.e. often clients do not know how to recover from a {@link JsonParseException}.</p>
        @author Inderjeet Singh
        @author Joel Leitch

# File: `Gson.java`

## Method: `public TypeAdapter<T> getAdapter(TypeToken<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public TypeAdapter<T> getAdapter(TypeToken<T> type)", "entityFile": "Gson.java"} -->Returns the type adapter for {@code} type.
        @throws IllegalArgumentException if this GSON cannot serialize and
        deserialize {@code type}.

# File: `JsonParser.java`

## Method: `public JsonElement parse(String json) throws JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement parse(String json) throws JsonSyntaxException", "entityFile": "JsonParser.java"} -->Parses the specified JSON string into a parse tree
        @param json JSON text
        @return a parse tree of {@link JsonElement}s corresponding to the specified JSON
        @throws JsonParseException if the specified text is not valid JSON
        @since 1.3

## Method: `public JsonElement parse(Reader json) throws JsonIOException, JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement parse(Reader json) throws JsonIOException, JsonSyntaxException", "entityFile": "JsonParser.java"} -->Parses the specified JSON string into a parse tree
        @param json JSON text
        @return a parse tree of {@link JsonElement}s corresponding to the specified JSON
        @throws JsonParseException if the specified text is not valid JSON
        @since 1.3

## Method: `public JsonElement parse(JsonReader json) throws JsonIOException, JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement parse(JsonReader json) throws JsonIOException, JsonSyntaxException", "entityFile": "JsonParser.java"} -->Returns the next value from the JSON stream as a parse tree.
        @throws JsonParseException if there is an IOException or if the specified
        text is not valid JSON
        @since 1.6

## Class: `JsonParser`

        <!-- META {"entityType": "Class", "entitySignature": "JsonParser", "entityFile": "JsonParser.java"} -->A parser to parse Json into a parse tree of {@link JsonElement}s
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.3

# File: `Gson.java`

## Method: `public TypeAdapter<T> getDelegateAdapter(TypeAdapterFactory skipPast, TypeToken<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public TypeAdapter<T> getDelegateAdapter(TypeAdapterFactory skipPast, TypeToken<T> type)", "entityFile": "Gson.java"} -->This method is used to get an alternate type adapter for the specified type. This is used
        to access a type adapter that is overridden by a {@link TypeAdapterFactory} that you
        may have registered. This features is typically used when you want to register a type
        adapter that does a little bit of work but then delegates further processing to the Gson
        default type adapter. Here is an example:
        <p>Let's say we want to write a type adapter that counts the number of objects being read
        from or written to JSON. We can achieve this by writing a type adapter factory that uses
        the <code>getDelegateAdapter</code> method:
        <pre> {@code
        class StatsTypeAdapterFactory implements TypeAdapterFactory {
        public int numReads = 0;
        public int numWrites = 0;
        public &lt;T&gt; TypeAdapter&lt;T&gt; create(Gson gson, TypeToken&lt;T&gt; type) {
        final TypeAdapter&lt;T&gt; delegate = gson.getDelegateAdapter(this, type);
        return new TypeAdapter&lt;T&gt;() {
        public void write(JsonWriter out, T value) throws IOException {
        ++numWrites;
        delegate.write(out, value);
        }
        public T read(JsonReader in) throws IOException {
        ++numReads;
        return delegate.read(in);
        }
        };
        }
        }
        } </pre>
        This factory can now be used like this:
        <pre> {@code
        StatsTypeAdapterFactory stats = new StatsTypeAdapterFactory();
        Gson gson = new GsonBuilder().registerTypeAdapterFactory(stats).create();
        // Call gson.toJson() and fromJson methods on objects
        System.out.println("Num JSON reads" + stats.numReads);
        System.out.println("Num JSON writes" + stats.numWrites);
        }</pre>
        Note that this call will skip all factories registered before {@code skipPast}. In case of
        multiple TypeAdapterFactories registered it is up to the caller of this function to insure
        that the order of registration does not prevent this method from reaching a factory they
        would expect to reply from this call.
        Note that since you can not override type adapter factories for String and Java primitive
        types, our stats factory will not count the number of String or primitives that will be
        read or written.
        @param skipPast The type adapter factory that needs to be skipped while searching for
        a matching type adapter. In most cases, you should just pass <i>this</i> (the type adapter
        factory from where {@link #getDelegateAdapter} method is being invoked).
        @param type Type for which the delegate adapter is being searched for.
        @since 2.2

# File: `None`

## None: `None`

        <!-- META {} -->Do NOT use any class in this package as they are meant for internal use in Gson.
        These classes will very likely change incompatibly in future versions. You have been warned.
        @author Inderjeet Singh, Joel Leitch, Jesse Wilson
        */
        package com.google.gson.internal;
        (package-info.java)
        Do NOT use any class in this package as they are meant for internal use in Gson.
        These classes will very likely change incompatibly in future versions. You have been warned.
        @author Inderjeet Singh, Joel Leitch, Jesse Wilson

# File: `Gson.java`

## Method: `public TypeAdapter<T> getAdapter(Class<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public TypeAdapter<T> getAdapter(Class<T> type)", "entityFile": "Gson.java"} -->Returns the type adapter for {@code} type.
        @throws IllegalArgumentException if this GSON cannot serialize and
        deserialize {@code type}.

## Method: `public JsonElement toJsonTree(Object src)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement toJsonTree(Object src)", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ea-8c1c-333445793454 <=< ACCEPT -->This method serializes the specified object into its equivalent representation as a tree of
        {@link JsonElement}s. This method should be used when the specified object is not a generic
        type. This method uses {@link Class#getClass()} to get the type for the specified object, but
        the {@code getClass()} loses the generic type information because of the Type Erasure feature
        of Java. Note that this method works fine if the any of the object fields are of generic type,
        just the object itself should not be of a generic type. If the object is of generic type, use
        {@link #toJsonTree(Object, Type)} instead.
        @param src the object for which Json representation is to be created setting for Gson
        @return Json representation of {@code src}.
        @since 1.4<!-- ACCEPT >=> f2e2218f-173e-11ea-8c1c-333445793454 -->

## Method: `public JsonElement toJsonTree(Object src, Type typeOfSrc)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement toJsonTree(Object src, Type typeOfSrc)", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ea-9c1c-333445793454 <=< ACCEPT -->This method serializes the specified object, including those of generic types, into its
        equivalent representation as a tree of {@link JsonElement}s. This method must be used if the
        specified object is a generic type. For non-generic objects, use {@link #toJsonTree(Object)}
        instead.
        @param src the object for which JSON representation is to be created
        @param typeOfSrc The specific genericized type of src. You can obtain
        this type by using the {@link com.google.gson.reflect.TypeToken} class. For example,
        to get the type for {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @return Json representation of {@code src}
        @since 1.4<!-- ACCEPT >=> f2e2218f-173e-11ea-9c1c-333445793454 -->

## Method: `public String toJson(Object src)`

        <!-- META {"entityType": "Method", "entitySignature": "public String toJson(Object src)", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ea-8c1c-333445793454 <=< ACCEPT -->This method serializes the specified object into its equivalent Json representation.
        This method should be used when the specified object is not a generic type. This method uses
        {@link Class#getClass()} to get the type for the specified object, but the
        {@code getClass()} loses the generic type information because of the Type Erasure feature
        of Java. Note that this method works fine if the any of the object fields are of generic type,
        just the object itself should not be of a generic type. If the object is of generic type, use
        {@link #toJson(Object, Type)} instead. If you want to write out the object to a
        {@link Writer}, use {@link #toJson(Object, Appendable)} instead.
        @param src the object for which Json representation is to be created setting for Gson
        @return Json representation of {@code src}.<!-- ACCEPT >=> f2e2218f-173e-11ea-8c1c-333445793454 -->

# File: `Primitives.java`

## Field: `PRIMITIVE_TO_WRAPPER_TYPE`

        <!-- META {"entityType": "Field", "entitySignature": "PRIMITIVE_TO_WRAPPER_TYPE", "entityFile": "Primitives.java"} -->A map from primitive types to their corresponding wrapper types.

# File: `Gson.java`

## Method: `public String toJson(Object src, Type typeOfSrc)`

        <!-- META {"entityType": "Method", "entitySignature": "public String toJson(Object src, Type typeOfSrc)", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ea-9c1c-333445793454 <=< ACCEPT -->This method serializes the specified object, including those of generic types, into its
        equivalent Json representation. This method must be used if the specified object is a generic
        type. For non-generic objects, use {@link #toJson(Object)} instead. If you want to write out
        the object to a {@link Appendable}, use {@link #toJson(Object, Type, Appendable)} instead.
        @param src the object for which JSON representation is to be created
        @param typeOfSrc The specific genericized type of src. You can obtain
        this type by using the {@link com.google.gson.reflect.TypeToken} class. For example,
        to get the type for {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @return Json representation of {@code src}<!-- ACCEPT >=> f2e2218f-173e-11ea-9c1c-333445793454 -->

# File: `Primitives.java`

## Field: `WRAPPER_TO_PRIMITIVE_TYPE`

        <!-- META {"entityType": "Field", "entitySignature": "WRAPPER_TO_PRIMITIVE_TYPE", "entityFile": "Primitives.java"} -->A map from wrapper types to their corresponding primitive types.

# File: `Gson.java`

## Method: `public void toJson(Object src, Appendable writer) throws JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void toJson(Object src, Appendable writer) throws JsonIOException", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ec-8c1c-333445793454 <=< ACCEPT -->This method serializes the specified object into its equivalent Json representation.
        This method should be used when the specified object is not a generic type. This method uses
        {@link Class#getClass()} to get the type for the specified object, but the
        {@code getClass()} loses the generic type information because of the Type Erasure feature
        of Java. Note that this method works fine if the any of the object fields are of generic type,
        just the object itself should not be of a generic type. If the object is of generic type, use
        {@link #toJson(Object, Type, Appendable)} instead.
        @param src the object for which Json representation is to be created setting for Gson
        @param writer Writer to which the Json representation needs to be written
        @throws JsonIOException if there was a problem writing to the writer
        @since 1.2<!-- ACCEPT >=> f2e2218f-173e-11ec-8c1c-333445793454 -->

# File: `Primitives.java`

## Method: `public static boolean isPrimitive(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean isPrimitive(Type type)", "entityFile": "Primitives.java"} -->Returns true if this type is a primitive.

## Method: `public static boolean isWrapperType(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean isWrapperType(Type type)", "entityFile": "Primitives.java"} -->Returns {@code true} if {@code type} is one of the nine
        primitive-wrapper types, such as {@link Integer}.
        @see Class#isPrimitive

# File: `Gson.java`

## Method: `public void toJson(Object src, Type typeOfSrc, Appendable writer) throws JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void toJson(Object src, Type typeOfSrc, Appendable writer) throws JsonIOException", "entityFile": "Gson.java"} --><!-- f2e2218f-173e-11ec-8c1c-333445793454 <=< ACCEPT -->This method serializes the specified object, including those of generic types, into its
        equivalent Json representation. This method must be used if the specified object is a generic
        type. For non-generic objects, use {@link #toJson(Object, Appendable)} instead.
        @param src the object for which JSON representation is to be created
        @param typeOfSrc The specific genericized type of src. You can obtain
        this type by using the {@link com.google.gson.reflect.TypeToken} class. For example,
        to get the type for {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @param writer Writer to which the Json representation of src needs to be written.
        @throws JsonIOException if there was a problem writing to the writer
        @since 1.2<!-- ACCEPT >=> f2e2218f-173e-11ec-8c1c-333445793454 -->

## Method: `public void toJson(Object src, Type typeOfSrc, JsonWriter writer) throws JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void toJson(Object src, Type typeOfSrc, JsonWriter writer) throws JsonIOException", "entityFile": "Gson.java"} -->Writes the JSON representation of {@code src} of type {@code typeOfSrc} to
        {@code writer}.
        @throws JsonIOException if there was a problem writing to the writer

## Method: `public String toJson(JsonElement jsonElement)`

        <!-- META {"entityType": "Method", "entitySignature": "public String toJson(JsonElement jsonElement)", "entityFile": "Gson.java"} -->Converts a tree of {@link JsonElement}s into its equivalent JSON representation.
        @param jsonElement root of a tree of {@link JsonElement}s
        @return JSON String representation of the tree
        @since 1.4

# File: `Primitives.java`

## Method: `public static Class<T> wrap(Class<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class<T> wrap(Class<T> type)", "entityFile": "Primitives.java"} -->Returns the corresponding wrapper type of {@code type} if it is a primitive
        type; otherwise returns {@code type} itself. Idempotent.
        <pre>
        wrap(int.class) == Integer.class
        wrap(Integer.class) == Integer.class
        wrap(String.class) == String.class
        </pre>

# File: `Gson.java`

## Method: `public void toJson(JsonElement jsonElement, Appendable writer) throws JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void toJson(JsonElement jsonElement, Appendable writer) throws JsonIOException", "entityFile": "Gson.java"} -->Writes out the equivalent JSON for a tree of {@link JsonElement}s.
        @param jsonElement root of a tree of {@link JsonElement}s
        @param writer Writer to which the Json representation needs to be written
        @throws JsonIOException if there was a problem writing to the writer
        @since 1.4

# File: `Primitives.java`

## Method: `public static Class<T> unwrap(Class<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Class<T> unwrap(Class<T> type)", "entityFile": "Primitives.java"} -->Returns the corresponding primitive type of {@code type} if it is a
        wrapper type; otherwise returns {@code type} itself. Idempotent.
        <pre>
        unwrap(Integer.class) == int.class
        unwrap(int.class) == int.class
        unwrap(String.class) == String.class
        </pre>

# File: `Gson.java`

## Method: `public JsonWriter newJsonWriter(Writer writer) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter newJsonWriter(Writer writer) throws IOException", "entityFile": "Gson.java"} -->Returns a new JSON writer configured for the settings on this Gson instance.

# File: `Primitives.java`

## Class: `Primitives`

        <!-- META {"entityType": "Class", "entitySignature": "Primitives", "entityFile": "Primitives.java"} -->Contains static utility methods pertaining to primitive types and their
        corresponding wrapper types.
        @author Kevin Bourrillion

# File: `Gson.java`

## Method: `public JsonReader newJsonReader(Reader reader)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonReader newJsonReader(Reader reader)", "entityFile": "Gson.java"} -->Returns a new JSON writer configured for the settings on this Gson instance.

## Method: `public void toJson(JsonElement jsonElement, JsonWriter writer) throws JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void toJson(JsonElement jsonElement, JsonWriter writer) throws JsonIOException", "entityFile": "Gson.java"} -->Writes the JSON for {@code jsonElement} to {@code writer}.
        @throws JsonIOException if there was a problem writing to the writer

# File: `Streams.java`

## Method: `public static JsonElement parse(JsonReader reader) throws JsonParseException`

        <!-- META {"entityType": "Method", "entitySignature": "public static JsonElement parse(JsonReader reader) throws JsonParseException", "entityFile": "Streams.java"} -->Takes a reader in any state and returns the next value as a JsonElement.

## Method: `public static void write(JsonElement element, JsonWriter writer) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public static void write(JsonElement element, JsonWriter writer) throws IOException", "entityFile": "Streams.java"} -->Writes the JSON element to the writer, recursively.

## Class: `CurrentWrite`

        <!-- META {"entityType": "Class", "entitySignature": "CurrentWrite", "entityFile": "Streams.java"} -->A mutable char sequence pointing at a single char[].

## Class: `AppendableWriter`

        <!-- META {"entityType": "Class", "entitySignature": "AppendableWriter", "entityFile": "Streams.java"} -->Adapts an {@link Appendable} so it can be passed anywhere a {@link Writer}
        is used.

## Class: `Streams`

        <!-- META {"entityType": "Class", "entitySignature": "Streams", "entityFile": "Streams.java"} -->Reads and writes GSON parse trees over streams.

# File: `Gson.java`

## Method: `public T fromJson(String json, Class<T> classOfT) throws JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(String json, Class<T> classOfT) throws JsonSyntaxException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11ea-84dc-333445793454 <=< ACCEPT -->This method deserializes the specified Json into an object of the specified class. It is not
        suitable to use if the specified class is a generic type since it will not have the generic
        type information because of the Type Erasure feature of Java. Therefore, this method should not
        be used if the desired type is a generic type. Note that this method works fine if the any of
        the fields of the specified object are generics, just the object itself should not be a
        generic type. For the cases when the object is of generic type, invoke
        {@link #fromJson(String, Type)}. If you have the Json in a {@link Reader} instead of
        a String, use {@link #fromJson(Reader, Class)} instead.
        @param <T> the type of the desired object
        @param json the string from which the object is to be deserialized
        @param classOfT the class of T
        @return an object of type T from the string. Returns {@code null} if {@code json} is {@code null}.
        @throws JsonSyntaxException if json is not a valid representation for an object of type
        classOfT<!-- ACCEPT >=> 22cae5c6-1734-11ea-84dc-333445793454 -->

## Method: `public T fromJson(String json, Type typeOfT) throws JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(String json, Type typeOfT) throws JsonSyntaxException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11eb-84dc-333445793454 <=< ACCEPT -->This method deserializes the specified Json into an object of the specified type. This method
        is useful if the specified object is a generic type. For non-generic objects, use
        {@link #fromJson(String, Class)} instead. If you have the Json in a {@link Reader} instead of
        a String, use {@link #fromJson(Reader, Type)} instead.
        @param <T> the type of the desired object
        @param json the string from which the object is to be deserialized
        @param typeOfT The specific genericized type of src. You can obtain this type by using the
        {@link com.google.gson.reflect.TypeToken} class. For example, to get the type for
        {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfT = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @return an object of type T from the string. Returns {@code null} if {@code json} is {@code null}.
        @throws JsonParseException if json is not a valid representation for an object of type typeOfT
        @throws JsonSyntaxException if json is not a valid representation for an object of type<!-- ACCEPT >=> 22cae5c6-1734-11eb-84dc-333445793454 -->

## Method: `public T fromJson(Reader json, Class<T> classOfT) throws JsonSyntaxException, JsonIOException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(Reader json, Class<T> classOfT) throws JsonSyntaxException, JsonIOException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11ea-84dc-333445793454 <=< ACCEPT -->This method deserializes the Json read from the specified reader into an object of the
        specified class. It is not suitable to use if the specified class is a generic type since it
        will not have the generic type information because of the Type Erasure feature of Java.
        Therefore, this method should not be used if the desired type is a generic type. Note that
        this method works fine if the any of the fields of the specified object are generics, just the
        object itself should not be a generic type. For the cases when the object is of generic type,
        invoke {@link #fromJson(Reader, Type)}. If you have the Json in a String form instead of a
        {@link Reader}, use {@link #fromJson(String, Class)} instead.
        @param <T> the type of the desired object
        @param json the reader producing the Json from which the object is to be deserialized.
        @param classOfT the class of T
        @return an object of type T from the string. Returns {@code null} if {@code json} is at EOF.
        @throws JsonIOException if there was a problem reading from the Reader
        @throws JsonSyntaxException if json is not a valid representation for an object of type
        @since 1.2<!-- ACCEPT >=> 22cae5c6-1734-11ea-84dc-333445793454 -->

## Method: `public T fromJson(Reader json, Type typeOfT) throws JsonIOException, JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(Reader json, Type typeOfT) throws JsonIOException, JsonSyntaxException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11eb-84dc-333445793454 <=< ACCEPT -->This method deserializes the Json read from the specified reader into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use {@link #fromJson(Reader, Class)} instead. If you have the Json in a
        String form instead of a {@link Reader}, use {@link #fromJson(String, Type)} instead.
        @param <T> the type of the desired object
        @param json the reader producing Json from which the object is to be deserialized
        @param typeOfT The specific genericized type of src. You can obtain this type by using the
        {@link com.google.gson.reflect.TypeToken} class. For example, to get the type for
        {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfT = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @return an object of type T from the json. Returns {@code null} if {@code json} is at EOF.
        @throws JsonIOException if there was a problem reading from the Reader
        @throws JsonSyntaxException if json is not a valid representation for an object of type
        @since 1.2<!-- ACCEPT >=> 22cae5c6-1734-11eb-84dc-333445793454 -->

## Method: `public T fromJson(JsonReader reader, Type typeOfT) throws JsonIOException, JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(JsonReader reader, Type typeOfT) throws JsonIOException, JsonSyntaxException", "entityFile": "Gson.java"} -->Reads the next JSON value from {@code reader} and convert it to an object
        of type {@code typeOfT}. Returns {@code null}, if the {@code reader} is at EOF.
        Since Type is not parameterized by T, this method is type unsafe and should be used carefully
        @throws JsonIOException if there was a problem writing to the Reader
        @throws JsonSyntaxException if json is not a valid representation for an object of type

## Method: `public T fromJson(JsonElement json, Class<T> classOfT) throws JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(JsonElement json, Class<T> classOfT) throws JsonSyntaxException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11ea-84dc-333445793454 <=< ACCEPT -->This method deserializes the Json read from the specified parse tree into an object of the
        specified type. It is not suitable to use if the specified class is a generic type since it
        will not have the generic type information because of the Type Erasure feature of Java.
        Therefore, this method should not be used if the desired type is a generic type. Note that
        this method works fine if the any of the fields of the specified object are generics, just the
        object itself should not be a generic type. For the cases when the object is of generic type,
        invoke {@link #fromJson(JsonElement, Type)}.
        @param <T> the type of the desired object
        @param json the root of the parse tree of {@link JsonElement}s from which the object is to
        be deserialized
        @param classOfT The class of T
        @return an object of type T from the json. Returns {@code null} if {@code json} is {@code null}.
        @throws JsonSyntaxException if json is not a valid representation for an object of type typeOfT
        @since 1.3<!-- ACCEPT >=> 22cae5c6-1734-11ea-84dc-333445793454 -->

# File: `JsonReader.java`

## Field: `NON_EXECUTE_PREFIX`

        <!-- META {"entityType": "Field", "entitySignature": "NON_EXECUTE_PREFIX", "entityFile": "JsonReader.java"} -->The only non-execute prefix this parser permits

## Field: `PEEKED_BUFFERED`

        <!-- META {"entityType": "Field", "entitySignature": "PEEKED_BUFFERED", "entityFile": "JsonReader.java"} -->When this is returned, the string value is stored in peekedString.

## Field: `PEEKED_LONG`

        <!-- META {"entityType": "Field", "entitySignature": "PEEKED_LONG", "entityFile": "JsonReader.java"} -->When this is returned, the integer value is stored in peekedLong.

## Field: `in`

        <!-- META {"entityType": "Field", "entitySignature": "in", "entityFile": "JsonReader.java"} -->The input JSON.

## Field: `lenient`

        <!-- META {"entityType": "Field", "entitySignature": "lenient", "entityFile": "JsonReader.java"} -->True to accept non-spec compliant JSON

## Field: `buffer`

        <!-- META {"entityType": "Field", "entitySignature": "buffer", "entityFile": "JsonReader.java"} -->Use a manual buffer to easily read and unread upcoming characters, and
        also so we can create strings without an intermediate StringBuilder.
        We decode literals directly out of this buffer, so it must be at least as
        long as the longest token that can be reported as a number.

## Field: `peekedLong`

        <!-- META {"entityType": "Field", "entitySignature": "peekedLong", "entityFile": "JsonReader.java"} -->A peeked value that was composed entirely of digits with an optional
        leading dash. Positive values may not have a leading 0.

## Field: `peekedNumberLength`

        <!-- META {"entityType": "Field", "entitySignature": "peekedNumberLength", "entityFile": "JsonReader.java"} -->The number of characters in a peeked number literal. Increment 'pos' by
        this after reading a number.

## Field: `peekedString`

        <!-- META {"entityType": "Field", "entitySignature": "peekedString", "entityFile": "JsonReader.java"} -->A peeked string that should be parsed on the next double, long or string.
        This is populated before a numeric value is parsed and used if that parsing
        fails.

## Method: `public JsonReader(Reader in)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonReader(Reader in)", "entityFile": "JsonReader.java"} -->Creates a new instance that reads a JSON-encoded stream from {@code in}.

# File: `UnsafeAllocator.java`

## Class: `UnsafeAllocator`

        <!-- META {"entityType": "Class", "entitySignature": "UnsafeAllocator", "entityFile": "UnsafeAllocator.java"} -->Do sneaky things to allocate objects without invoking their constructors.
        @author Joel Leitch
        @author Jesse Wilson

# File: `JsonReader.java`

## Method: `public final void setLenient(boolean lenient)`

        <!-- META {"entityType": "Method", "entitySignature": "public final void setLenient(boolean lenient)", "entityFile": "JsonReader.java"} -->Configure this parser to be liberal in what it accepts. By default,
        this parser is strict and only accepts JSON as specified by <a
        href="http://www.ietf.org/rfc/rfc4627.txt">RFC 4627</a>. Setting the
        parser to lenient causes it to ignore the following syntax errors:
        <ul>
        <li>Streams that start with the <a href="#nonexecuteprefix">non-execute
        prefix</a>, <code>")]}'\n"</code>.
        <li>Streams that include multiple top-level values. With strict parsing,
        each stream must contain exactly one top-level value.
        <li>Top-level values of any type. With strict parsing, the top-level
        value must be an object or an array.
        <li>Numbers may be {@link Double#isNaN() NaNs} or {@link
        Double#isInfinite() infinities}.
        <li>End of line comments starting with {@code //} or {@code #} and
        ending with a newline character.
        <li>C-style comments starting with {@code /*} and ending with
        {@code *}{@code /}. Such comments may not be nested.
        <li>Names that are unquoted or {@code 'single quoted'}.
        <li>Strings that are unquoted or {@code 'single quoted'}.
        <li>Array elements separated by {@code ;} instead of {@code ,}.
        <li>Unnecessary array separators. These are interpreted as if null
        was the omitted value.
        <li>Names and values separated by {@code =} or {@code =>} instead of
        {@code :}.
        <li>Name/value pairs separated by {@code ;} instead of {@code ,}.
        </ul>

## Method: `public final boolean isLenient()`

        <!-- META {"entityType": "Method", "entitySignature": "public final boolean isLenient()", "entityFile": "JsonReader.java"} -->Returns true if this parser is liberal in what it accepts.

## Method: `public void beginArray() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void beginArray() throws IOException", "entityFile": "JsonReader.java"} --><!-- a8176282-175c-11ea-a797-333445793454 <=< ACCEPT -->Consumes the next token from the JSON stream and asserts that it is the
        beginning of a new array.<!-- ACCEPT >=> a8176282-175c-11ea-a797-333445793454 -->

## Method: `public void endArray() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void endArray() throws IOException", "entityFile": "JsonReader.java"} --><!-- a8176282-175c-11ea-a797-333445793454 <=< ACCEPT -->Consumes the next token from the JSON stream and asserts that it is the
        end of the current array.<!-- ACCEPT >=> a8176282-175c-11ea-a797-333445793454 -->

## Method: `public void beginObject() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void beginObject() throws IOException", "entityFile": "JsonReader.java"} --><!-- a8176282-175c-11ea-a797-333445793454 <=< ACCEPT -->Consumes the next token from the JSON stream and asserts that it is the
        beginning of a new object.<!-- ACCEPT >=> a8176282-175c-11ea-a797-333445793454 -->

## Method: `public void endObject() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void endObject() throws IOException", "entityFile": "JsonReader.java"} --><!-- a8176282-175c-11ea-a797-333445793454 <=< ACCEPT -->Consumes the next token from the JSON stream and asserts that it is the
        end of the current object.<!-- ACCEPT >=> a8176282-175c-11ea-a797-333445793454 -->

## Method: `public boolean hasNext() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasNext() throws IOException", "entityFile": "JsonReader.java"} -->Returns true if the current array or object has another element.

## Method: `public JsonToken peek() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonToken peek() throws IOException", "entityFile": "JsonReader.java"} -->Returns the type of the next token without consuming it.

## Method: `public String nextName() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public String nextName() throws IOException", "entityFile": "JsonReader.java"} -->Returns the next token, a {@link com.google.gson.stream.JsonToken#NAME property name}, and
        consumes it.
        @throws java.io.IOException if the next token in the stream is not a property
        name.

## Method: `public String nextString() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public String nextString() throws IOException", "entityFile": "JsonReader.java"} --><!-- b515fdb8-175c-11ea-a04a-333445793454 <=< ACCEPT -->Returns the {@link com.google.gson.stream.JsonToken#STRING string} value of the next token,
        consuming it. If the next token is a number, this method will return its
        string form.
        @throws IllegalStateException if the next token is not a string or if
        this reader is closed.<!-- ACCEPT >=> b515fdb8-175c-11ea-a04a-333445793454 -->

## Method: `public boolean nextBoolean() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean nextBoolean() throws IOException", "entityFile": "JsonReader.java"} --><!-- b515fdb8-175c-11ea-a04a-333445793454 <=< ACCEPT -->Returns the {@link com.google.gson.stream.JsonToken#BOOLEAN boolean} value of the next token,
        consuming it.
        @throws IllegalStateException if the next token is not a boolean or if
        this reader is closed.<!-- ACCEPT >=> b515fdb8-175c-11ea-a04a-333445793454 -->

## Method: `public void nextNull() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void nextNull() throws IOException", "entityFile": "JsonReader.java"} -->Consumes the next token from the JSON stream and asserts that it is a
        literal null.
        @throws IllegalStateException if the next token is not null or if this
        reader is closed.

## Method: `public double nextDouble() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public double nextDouble() throws IOException", "entityFile": "JsonReader.java"} --><!-- b515fdb8-175c-11eb-a04a-333445793454 <=< ACCEPT -->Returns the {@link com.google.gson.stream.JsonToken#NUMBER double} value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as a double using {@link Double#parseDouble(String)}.
        @throws IllegalStateException if the next token is not a literal value.
        @throws NumberFormatException if the next literal value cannot be parsed
        as a double, or is non-finite.<!-- ACCEPT >=> b515fdb8-175c-11eb-a04a-333445793454 -->

# File: `LazilyParsedNumber.java`

## Method: `public LazilyParsedNumber(String value)`

        <!-- META {"entityType": "Method", "entitySignature": "public LazilyParsedNumber(String value)", "entityFile": "LazilyParsedNumber.java"} -->@param value must not be null

## Method: `private Object writeReplace() throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "private Object writeReplace() throws ObjectStreamException", "entityFile": "LazilyParsedNumber.java"} -->If somebody is unlucky enough to have to serialize one of these, serialize
        it as a BigDecimal so that they won't need Gson on the other side to
        deserialize it.

## Class: `LazilyParsedNumber`

        <!-- META {"entityType": "Class", "entitySignature": "LazilyParsedNumber", "entityFile": "LazilyParsedNumber.java"} -->This class holds a number value that is lazily converted to a specific number type
        @author Inderjeet Singh

# File: `TypeAdapters.java`

## Field: `BOOLEAN_AS_STRING`

        <!-- META {"entityType": "Field", "entitySignature": "BOOLEAN_AS_STRING", "entityFile": "TypeAdapters.java"} -->Writes a boolean as a string. Useful for map keys, where booleans aren't
        otherwise permitted.

## Method: `public static TypeAdapterFactory newTypeHierarchyFactory(final Class<T1> clazz, final TypeAdapter<T1> typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeAdapterFactory newTypeHierarchyFactory(final Class<T1> clazz, final TypeAdapter<T1> typeAdapter)", "entityFile": "TypeAdapters.java"} -->Returns a factory for all subtypes of {@code typeAdapter}. We do a runtime check to confirm
        that the deserialized type matches the type requested.

# File: `Gson.java`

## Method: `public T fromJson(JsonElement json, Type typeOfT) throws JsonSyntaxException`

        <!-- META {"entityType": "Method", "entitySignature": "public T fromJson(JsonElement json, Type typeOfT) throws JsonSyntaxException", "entityFile": "Gson.java"} --><!-- 22cae5c6-1734-11eb-84dc-333445793454 <=< ACCEPT -->This method deserializes the Json read from the specified parse tree into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use {@link #fromJson(JsonElement, Class)} instead.
        @param <T> the type of the desired object
        @param json the root of the parse tree of {@link JsonElement}s from which the object is to
        be deserialized
        @param typeOfT The specific genericized type of src. You can obtain this type by using the
        {@link com.google.gson.reflect.TypeToken} class. For example, to get the type for
        {@code Collection<Foo>}, you should use:
        <pre>
        Type typeOfT = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        </pre>
        @return an object of type T from the json. Returns {@code null} if {@code json} is {@code null}.
        @throws JsonSyntaxException if json is not a valid representation for an object of type typeOfT
        @since 1.3<!-- ACCEPT >=> 22cae5c6-1734-11eb-84dc-333445793454 -->

# File: `TypeAdapters.java`

## Class: `TypeAdapters`

        <!-- META {"entityType": "Class", "entitySignature": "TypeAdapters", "entityFile": "TypeAdapters.java"} -->Type adapters for basic types.

# File: `Gson.java`

## Class: `Gson`

        <!-- META {"entityType": "Class", "entitySignature": "Gson", "entityFile": "Gson.java"} -->This is the main class for using Gson. Gson is typically used by first constructing a
        Gson instance and then invoking {@link #toJson(Object)} or {@link #fromJson(String, Class)}
        methods on it. Gson instances are Thread-safe so you can reuse them freely across multiple
        threads.
        <p>You can create a Gson instance by invoking {@code new Gson()} if the default configuration
        is all you need. You can also use {@link GsonBuilder} to build a Gson instance with various
        configuration options such as versioning support, pretty printing, custom
        {@link JsonSerializer}s, {@link JsonDeserializer}s, and {@link InstanceCreator}s.</p>
        <p>Here is an example of how Gson is used for a simple Class:
        <pre>
        Gson gson = new Gson(); // Or use new GsonBuilder().create();
        MyType target = new MyType();
        String json = gson.toJson(target); // serializes target to Json
        MyType target2 = gson.fromJson(json, MyType.class); // deserializes json into target2
        </pre></p>
        <p>If the object that your are serializing/deserializing is a {@code ParameterizedType}
        (i.e. contains at least one type parameter and may be an array) then you must use the
        {@link #toJson(Object, Type)} or {@link #fromJson(String, Type)} method.  Here is an
        example for serializing and deserializing a {@code ParameterizedType}:
        <pre>
        Type listType = new TypeToken&lt;List&lt;String&gt;&gt;() {}.getType();
        List&lt;String&gt; target = new LinkedList&lt;String&gt;();
        target.add("blah");
        Gson gson = new Gson();
        String json = gson.toJson(target, listType);
        List&lt;String&gt; target2 = gson.fromJson(json, listType);
        </pre></p>
        <p>See the <a href="https://sites.google.com/site/gson/gson-user-guide">Gson User Guide</a>
        for a more complete set of examples.</p>
        @see com.google.gson.reflect.TypeToken
        @author Inderjeet Singh
        @author Joel Leitch
        @author Jesse Wilson

# File: `JsonReader.java`

## Method: `public long nextLong() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public long nextLong() throws IOException", "entityFile": "JsonReader.java"} --><!-- b515fdb8-175c-11eb-a04a-333445793454 <=< ACCEPT -->Returns the {@link com.google.gson.stream.JsonToken#NUMBER long} value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as a long. If the next token's numeric value cannot be exactly
        represented by a Java {@code long}, this method throws.
        @throws IllegalStateException if the next token is not a literal value.
        @throws NumberFormatException if the next literal value cannot be parsed
        as a number, or exactly represented as a long.<!-- ACCEPT >=> b515fdb8-175c-11eb-a04a-333445793454 -->

## Method: `private String nextQuotedValue(char quote) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private String nextQuotedValue(char quote) throws IOException", "entityFile": "JsonReader.java"} -->Returns the string up to but not including {@code quote}, unescaping any
        character escape sequences encountered along the way. The opening quote
        should have already been read. This consumes the closing quote, but does
        not include it in the returned string.
        @param quote either ' or ".
        @throws NumberFormatException if any unicode escape sequences are
        malformed.

## Method: `private String nextUnquotedValue() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private String nextUnquotedValue() throws IOException", "entityFile": "JsonReader.java"} -->Returns an unquoted value as a string.

## Method: `public int nextInt() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public int nextInt() throws IOException", "entityFile": "JsonReader.java"} --><!-- b515fdb8-175c-11eb-a04a-333445793454 <=< ACCEPT -->Returns the {@link com.google.gson.stream.JsonToken#NUMBER int} value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as an int. If the next token's numeric value cannot be exactly
        represented by a Java {@code int}, this method throws.
        @throws IllegalStateException if the next token is not a literal value.
        @throws NumberFormatException if the next literal value cannot be parsed
        as a number, or exactly represented as an int.<!-- ACCEPT >=> b515fdb8-175c-11eb-a04a-333445793454 -->

## Method: `public void close() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void close() throws IOException", "entityFile": "JsonReader.java"} -->Closes this JSON reader and the underlying {@link java.io.Reader}.

## Method: `public void skipValue() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void skipValue() throws IOException", "entityFile": "JsonReader.java"} -->Skips the next value recursively. If it is an object or array, all nested
        elements are skipped. This method is intended for use when the JSON token
        stream contains unrecognized or unhandled values.

## Method: `private boolean fillBuffer(int minimum) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private boolean fillBuffer(int minimum) throws IOException", "entityFile": "JsonReader.java"} -->Returns true once {@code limit - pos >= minimum}. If the data is
        exhausted before that many characters are available, this returns
        false.

## Method: `private int nextNonWhitespace(boolean throwOnEof) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private int nextNonWhitespace(boolean throwOnEof) throws IOException", "entityFile": "JsonReader.java"} -->Returns the next character in the stream that is neither whitespace nor a
        part of a comment. When this returns, the returned character is always at
        {@code buffer[pos-1]}; this means the caller can always push back the
        returned character by decrementing {@code pos}.

## Method: `private void skipToEndOfLine() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private void skipToEndOfLine() throws IOException", "entityFile": "JsonReader.java"} -->Advances the position until after the next newline character. If the line
        is terminated by "\r\n", the '\n' must be consumed as whitespace by the
        caller.

## Method: `private boolean skipTo(String toFind) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private boolean skipTo(String toFind) throws IOException", "entityFile": "JsonReader.java"} -->@param toFind a string to search for. Must not contain a newline.

## Method: `public String getPath()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getPath()", "entityFile": "JsonReader.java"} -->Returns a <a href="http://goessner.net/articles/JsonPath/">JsonPath</a> to
        the current location in the JSON value.

## Method: `private char readEscapeCharacter() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private char readEscapeCharacter() throws IOException", "entityFile": "JsonReader.java"} -->Unescapes the character identified by the character or characters that
        immediately follow a backslash. The backslash '\' should have already
        been read. This supports both unicode escapes "u000A" and two-character
        escapes "\n".
        @throws NumberFormatException if any unicode escape sequences are
        malformed.

## Method: `private IOException syntaxError(String message) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private IOException syntaxError(String message) throws IOException", "entityFile": "JsonReader.java"} -->Throws a new IO exception with the given message and a context snippet
        with this reader's content.

## Method: `private void consumeNonExecutePrefix() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private void consumeNonExecutePrefix() throws IOException", "entityFile": "JsonReader.java"} -->Consumes the non-execute prefix if it exists.

# File: `ISO8601Utils.java`

## Field: `UTC_ID`

        <!-- META {"entityType": "Field", "entitySignature": "UTC_ID", "entityFile": "ISO8601Utils.java"} -->ID to represent the 'UTC' string, default timezone since Jackson 2.7
        @since 2.7

# File: `GsonBuilder.java`

## Field: `hierarchyFactories`

        <!-- META {"entityType": "Field", "entitySignature": "hierarchyFactories", "entityFile": "GsonBuilder.java"} -->tree-style hierarchy factories. These come after factories for backwards compatibility.

# File: `ISO8601Utils.java`

## Field: `TIMEZONE_UTC`

        <!-- META {"entityType": "Field", "entitySignature": "TIMEZONE_UTC", "entityFile": "ISO8601Utils.java"} -->The UTC timezone, prefetched to avoid more lookups.
        @since 2.7

# File: `GsonBuilder.java`

## Method: `public GsonBuilder()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder()", "entityFile": "GsonBuilder.java"} -->Creates a GsonBuilder instance that can be used to build Gson with various configuration
        settings. GsonBuilder follows the builder pattern, and it is typically used by first
        invoking various configuration methods to set desired options, and finally calling
        {@link #create()}.

# File: `ISO8601Utils.java`

## Method: `public static String format(Date date)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String format(Date date)", "entityFile": "ISO8601Utils.java"} -->Format a date into 'yyyy-MM-ddThh:mm:ssZ' (default timezone, no milliseconds precision)
        @param date the date to format
        @return the date formatted as 'yyyy-MM-ddThh:mm:ssZ'

## Method: `public static String format(Date date, boolean millis)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String format(Date date, boolean millis)", "entityFile": "ISO8601Utils.java"} -->Format a date into 'yyyy-MM-ddThh:mm:ss[.sss]Z' (GMT timezone)
        @param date the date to format
        @param millis true to include millis precision otherwise false
        @return the date formatted as 'yyyy-MM-ddThh:mm:ss[.sss]Z'

# File: `GsonBuilder.java`

## Method: `public GsonBuilder setVersion(double ignoreVersionsAfter)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setVersion(double ignoreVersionsAfter)", "entityFile": "GsonBuilder.java"} -->Configures Gson to enable versioning support.
        @param ignoreVersionsAfter any field or type marked with a version higher than this value
        are ignored during serialization or deserialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern

## Method: `public GsonBuilder excludeFieldsWithModifiers(int... modifiers)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder excludeFieldsWithModifiers(int... modifiers)", "entityFile": "GsonBuilder.java"} -->Configures Gson to excludes all class fields that have the specified modifiers. By default,
        Gson will exclude all fields marked transient or static. This method will override that
        behavior.
        @param modifiers the field modifiers. You must use the modifiers specified in the
        {@link java.lang.reflect.Modifier} class. For example,
        {@link java.lang.reflect.Modifier#TRANSIENT},
        {@link java.lang.reflect.Modifier#STATIC}.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern

# File: `ISO8601Utils.java`

## Method: `public static String format(Date date, boolean millis, TimeZone tz)`

        <!-- META {"entityType": "Method", "entitySignature": "public static String format(Date date, boolean millis, TimeZone tz)", "entityFile": "ISO8601Utils.java"} -->Format date into yyyy-MM-ddThh:mm:ss[.sss][Z|[+-]hh:mm]
        @param date the date to format
        @param millis true to include millis precision otherwise false
        @param tz timezone to use for the formatting (UTC will produce 'Z')
        @return the date formatted as yyyy-MM-ddThh:mm:ss[.sss][Z|[+-]hh:mm]

# File: `GsonBuilder.java`

## Method: `public GsonBuilder generateNonExecutableJson()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder generateNonExecutableJson()", "entityFile": "GsonBuilder.java"} -->Makes the output JSON non-executable in Javascript by prefixing the generated JSON with some
        special text. This prevents attacks from third-party sites through script sourcing. See
        <a href="http://code.google.com/p/google-gson/issues/detail?id=42">Gson Issue 42</a>
        for details.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3

## Method: `public GsonBuilder excludeFieldsWithoutExposeAnnotation()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder excludeFieldsWithoutExposeAnnotation()", "entityFile": "GsonBuilder.java"} -->Configures Gson to exclude all fields from consideration for serialization or deserialization
        that do not have the {@link com.google.gson.annotations.Expose} annotation.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern

# File: `ISO8601Utils.java`

## Method: `public static Date parse(String date, ParsePosition pos) throws ParseException`

        <!-- META {"entityType": "Method", "entitySignature": "public static Date parse(String date, ParsePosition pos) throws ParseException", "entityFile": "ISO8601Utils.java"} -->Parse a date from ISO-8601 formatted string. It expects a format
        [yyyy-MM-dd|yyyyMMdd][T(hh:mm[:ss[.sss]]|hhmm[ss[.sss]])]?[Z|[+-]hh[:mm]]]
        @param date ISO string to parse in the appropriate format.
        @param pos The position to start parsing from, updated to where parsing stopped.
        @return the parsed date
        @throws ParseException if the date is not in the appropriate format

# File: `GsonBuilder.java`

## Method: `public GsonBuilder serializeNulls()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder serializeNulls()", "entityFile": "GsonBuilder.java"} -->Configure Gson to serialize null fields. By default, Gson omits all fields that are null
        during serialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.2

# File: `ISO8601Utils.java`

## Method: `private static boolean checkOffset(String value, int offset, char expected)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean checkOffset(String value, int offset, char expected)", "entityFile": "ISO8601Utils.java"} -->Check if the expected character exist at the given offset in the value.
        @param value the string to check at the specified offset
        @param offset the offset to look for the expected character
        @param expected the expected character
        @return true if the expected character exist at the given offset

## Method: `private static int parseInt(String value, int beginIndex, int endIndex) throws NumberFormatException`

        <!-- META {"entityType": "Method", "entitySignature": "private static int parseInt(String value, int beginIndex, int endIndex) throws NumberFormatException", "entityFile": "ISO8601Utils.java"} -->Parse an integer located between 2 given offsets in a string
        @param value the string to parse
        @param beginIndex the start index for the integer in the string
        @param endIndex the end index for the integer in the string
        @return the int
        @throws NumberFormatException if the value is not a number

## Method: `private static void padInt(StringBuilder buffer, int value, int length)`

        <!-- META {"entityType": "Method", "entitySignature": "private static void padInt(StringBuilder buffer, int value, int length)", "entityFile": "ISO8601Utils.java"} -->Zero pad a number to a specified length
        @param buffer buffer to use for padding
        @param value the integer value to pad if necessary.
        @param length the length of the string we should zero pad

# File: `GsonBuilder.java`

## Method: `public GsonBuilder enableComplexMapKeySerialization()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder enableComplexMapKeySerialization()", "entityFile": "GsonBuilder.java"} -->Enabling this feature will only change the serialized form if the map key is
        a complex type (i.e. non-primitive) in its <strong>serialized</strong> JSON
        form. The default implementation of map serialization uses {@code toString()}
        on the key; however, when this is called then one of the following cases
        apply:
        <h3>Maps as JSON objects</h3>
        For this case, assume that a type adapter is registered to serialize and
        deserialize some {@code Point} class, which contains an x and y coordinate,
        to/from the JSON Primitive string value {@code "(x,y)"}. The Java map would
        then be serialized as a {@link JsonObject}.
        <p>Below is an example:
        <pre>  {@code
        Gson gson = new GsonBuilder()
        .register(Point.class, new MyPointTypeAdapter())
        .enableComplexMapKeySerialization()
        .create();
        Map<Point, String> original = new LinkedHashMap<Point, String>();
        original.put(new Point(5, 6), "a");
        original.put(new Point(8, 8), "b");
        System.out.println(gson.toJson(original, type));
        }</pre>
        The above code prints this JSON object:<pre>  {@code
        {
        "(5,6)": "a",
        "(8,8)": "b"
        }
        }</pre>
        <h3>Maps as JSON arrays</h3>
        For this case, assume that a type adapter was NOT registered for some
        {@code Point} class, but rather the default Gson serialization is applied.
        In this case, some {@code new Point(2,3)} would serialize as {@code
        {"x":2,"y":5}}.
        <p>Given the assumption above, a {@code Map<Point, String>} will be
        serialize as an array of arrays (can be viewed as an entry set of pairs).
        <p>Below is an example of serializing complex types as JSON arrays:
        <pre> {@code
        Gson gson = new GsonBuilder()
        .enableComplexMapKeySerialization()
        .create();
        Map<Point, String> original = new LinkedHashMap<Point, String>();
        original.put(new Point(5, 6), "a");
        original.put(new Point(8, 8), "b");
        System.out.println(gson.toJson(original, type));
        }
        The JSON output would look as follows:
        <pre>   {@code
        [
        [
        {
        "x": 5,
        "y": 6
        },
        "a"
        ],
        [
        {
        "x": 8,
        "y": 8
        },
        "b"
        ]
        ]
        }</pre>
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.7

# File: `ISO8601Utils.java`

## Method: `private static int indexOfNonDigit(String string, int offset)`

        <!-- META {"entityType": "Method", "entitySignature": "private static int indexOfNonDigit(String string, int offset)", "entityFile": "ISO8601Utils.java"} -->Returns the index of the first character in the string that is not a digit, starting at offset.

# File: `JsonReader.java`

## Class: `JsonReader`

        <!-- META {"entityType": "Class", "entitySignature": "JsonReader", "entityFile": "JsonReader.java"} -->Reads a JSON (<a href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>)
        encoded value as a stream of tokens. This stream includes both literal
        values (strings, numbers, booleans, and nulls) as well as the begin and
        end delimiters of objects and arrays. The tokens are traversed in
        depth-first order, the same order that they appear in the JSON document.
        Within JSON objects, name/value pairs are represented by a single token.
        <h3>Parsing JSON</h3>
        To create a recursive descent parser for your own JSON streams, first create
        an entry point method that creates a {@code JsonReader}.
        <p>Next, create handler methods for each structure in your JSON text. You'll
        need a method for each object type and for each array type.
        <ul>
        <li>Within <strong>array handling</strong> methods, first call {@link
        #beginArray} to consume the array's opening bracket. Then create a
        while loop that accumulates values, terminating when {@link #hasNext}
        is false. Finally, read the array's closing bracket by calling {@link
        #endArray}.
        <li>Within <strong>object handling</strong> methods, first call {@link
        #beginObject} to consume the object's opening brace. Then create a
        while loop that assigns values to local variables based on their name.
        This loop should terminate when {@link #hasNext} is false. Finally,
        read the object's closing brace by calling {@link #endObject}.
        </ul>
        <p>When a nested object or array is encountered, delegate to the
        corresponding handler method.
        <p>When an unknown name is encountered, strict parsers should fail with an
        exception. Lenient parsers should call {@link #skipValue()} to recursively
        skip the value's nested tokens, which may otherwise conflict.
        <p>If a value may be null, you should first check using {@link #peek()}.
        Null literals can be consumed using either {@link #nextNull()} or {@link
        #skipValue()}.
        <h3>Example</h3>
        Suppose we'd like to parse a stream of messages such as the following: <pre> {@code
        [
        {
        "id": 912345678901,
        "text": "How do I read a JSON stream in Java?",
        "geo": null,
        "user": {
        "name": "json_newb",
        "followers_count": 41
        }
        },
        {
        "id": 912345678902,
        "text": "@json_newb just use JsonReader!",
        "geo": [50.454722, -104.606667],
        "user": {
        "name": "jesse",
        "followers_count": 2
        }
        }
        ]}</pre>
        This code implements the parser for the above structure: <pre>   {@code
        public List<Message> readJsonStream(InputStream in) throws IOException {
        JsonReader reader = new JsonReader(new InputStreamReader(in, "UTF-8"));
        try {
        return readMessagesArray(reader);
        } finally {
        reader.close();
        }
        }
        public List<Message> readMessagesArray(JsonReader reader) throws IOException {
        List<Message> messages = new ArrayList<Message>();
        reader.beginArray();
        while (reader.hasNext()) {
        messages.add(readMessage(reader));
        }
        reader.endArray();
        return messages;
        }
        public Message readMessage(JsonReader reader) throws IOException {
        long id = -1;
        String text = null;
        User user = null;
        List<Double> geo = null;
        reader.beginObject();
        while (reader.hasNext()) {
        String name = reader.nextName();
        if (name.equals("id")) {
        id = reader.nextLong();
        } else if (name.equals("text")) {
        text = reader.nextString();
        } else if (name.equals("geo") && reader.peek() != JsonToken.NULL) {
        geo = readDoublesArray(reader);
        } else if (name.equals("user")) {
        user = readUser(reader);
        } else {
        reader.skipValue();
        }
        }
        reader.endObject();
        return new Message(id, text, user, geo);
        }
        public List<Double> readDoublesArray(JsonReader reader) throws IOException {
        List<Double> doubles = new ArrayList<Double>();
        reader.beginArray();
        while (reader.hasNext()) {
        doubles.add(reader.nextDouble());
        }
        reader.endArray();
        return doubles;
        }
        public User readUser(JsonReader reader) throws IOException {
        String username = null;
        int followersCount = -1;
        reader.beginObject();
        while (reader.hasNext()) {
        String name = reader.nextName();
        if (name.equals("name")) {
        username = reader.nextString();
        } else if (name.equals("followers_count")) {
        followersCount = reader.nextInt();
        } else {
        reader.skipValue();
        }
        }
        reader.endObject();
        return new User(username, followersCount);
        }}</pre>
        <h3>Number Handling</h3>
        This reader permits numeric values to be read as strings and string values to
        be read as numbers. For example, both elements of the JSON array {@code
        [1, "1"]} may be read using either {@link #nextInt} or {@link #nextString}.
        This behavior is intended to prevent lossy numeric conversions: double is
        JavaScript's only numeric type and very large values like {@code
        9007199254740993} cannot be represented exactly on that platform. To minimize
        precision loss, extremely large values should be written and read as strings
        in JSON.
        <a name="nonexecuteprefix"/><h3>Non-Execute Prefix</h3>
        Web servers that serve private data using JSON may be vulnerable to <a
        href="http://en.wikipedia.org/wiki/JSON#Cross-site_request_forgery">Cross-site
        request forgery</a> attacks. In such an attack, a malicious site gains access
        to a private JSON file by executing it with an HTML {@code <script>} tag.
        <p>Prefixing JSON files with <code>")]}'\n"</code> makes them non-executable
        by {@code <script>} tags, disarming the attack. Since the prefix is malformed
        JSON, strict parsing fails when it is encountered. This class permits the
        non-execute prefix when {@link #setLenient(boolean) lenient parsing} is
        enabled.
        <p>Each {@code JsonReader} may be used to read a single JSON stream. Instances
        of this class are not thread safe.
        @author Jesse Wilson
        @since 1.6

# File: `JsonScope.java`

## Field: `EMPTY_ARRAY`

        <!-- META {"entityType": "Field", "entitySignature": "EMPTY_ARRAY", "entityFile": "JsonScope.java"} -->An array with no elements requires no separators or newlines before
        it is closed.

## Field: `NONEMPTY_ARRAY`

        <!-- META {"entityType": "Field", "entitySignature": "NONEMPTY_ARRAY", "entityFile": "JsonScope.java"} -->A array with at least one value requires a comma and newline before
        the next element.

## Field: `EMPTY_OBJECT`

        <!-- META {"entityType": "Field", "entitySignature": "EMPTY_OBJECT", "entityFile": "JsonScope.java"} -->An object with no name/value pairs requires no separators or newlines
        before it is closed.

## Field: `DANGLING_NAME`

        <!-- META {"entityType": "Field", "entitySignature": "DANGLING_NAME", "entityFile": "JsonScope.java"} -->An object whose most recent element is a key. The next element must
        be a value.

## Field: `NONEMPTY_OBJECT`

        <!-- META {"entityType": "Field", "entitySignature": "NONEMPTY_OBJECT", "entityFile": "JsonScope.java"} -->An object with at least one name/value pair requires a comma and
        newline before the next element.

## Field: `EMPTY_DOCUMENT`

        <!-- META {"entityType": "Field", "entitySignature": "EMPTY_DOCUMENT", "entityFile": "JsonScope.java"} -->No object or array has been started.

## Field: `NONEMPTY_DOCUMENT`

        <!-- META {"entityType": "Field", "entitySignature": "NONEMPTY_DOCUMENT", "entityFile": "JsonScope.java"} -->A document with at an array or object.

## Field: `CLOSED`

        <!-- META {"entityType": "Field", "entitySignature": "CLOSED", "entityFile": "JsonScope.java"} -->A document that's been closed and cannot be accessed.

## Class: `JsonScope`

        <!-- META {"entityType": "Class", "entitySignature": "JsonScope", "entityFile": "JsonScope.java"} -->Lexical scoping elements within a JSON reader or writer.
        @author Jesse Wilson
        @since 1.6

# File: `ConstructorConstructor.java`

## Method: `private ObjectConstructor<T> newDefaultImplementationConstructor(final Type type, Class<? super T> rawType)`

        <!-- META {"entityType": "Method", "entitySignature": "private ObjectConstructor<T> newDefaultImplementationConstructor(final Type type, Class<? super T> rawType)", "entityFile": "ConstructorConstructor.java"} -->Constructors for common interface types like Map and List and their
        subtypes.

## Class: `ConstructorConstructor`

        <!-- META {"entityType": "Class", "entitySignature": "ConstructorConstructor", "entityFile": "ConstructorConstructor.java"} -->Returns a function that can construct an instance of a requested type.

# File: `JsonToken.java`

## EnumConstant: `BEGIN_ARRAY`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "BEGIN_ARRAY", "entityFile": "JsonToken.java"} --><!-- e7bfa171-173f-11ea-a3d5-333445793454 <=< ACCEPT -->The opening of a JSON array. Written using {@link JsonWriter#beginArray}
        and read using {@link JsonReader#beginArray}.<!-- ACCEPT >=> e7bfa171-173f-11ea-a3d5-333445793454 -->

## EnumConstant: `END_ARRAY`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "END_ARRAY", "entityFile": "JsonToken.java"} --><!-- e7bfa171-173f-11ea-a3d5-333445793454 <=< ACCEPT -->The closing of a JSON array. Written using {@link JsonWriter#endArray}
        and read using {@link JsonReader#endArray}.<!-- ACCEPT >=> e7bfa171-173f-11ea-a3d5-333445793454 -->

## EnumConstant: `BEGIN_OBJECT`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "BEGIN_OBJECT", "entityFile": "JsonToken.java"} --><!-- e7bfa171-173f-11ea-a3d5-333445793454 <=< ACCEPT -->The opening of a JSON object. Written using {@link JsonWriter#beginObject}
        and read using {@link JsonReader#beginObject}.<!-- ACCEPT >=> e7bfa171-173f-11ea-a3d5-333445793454 -->

## EnumConstant: `END_OBJECT`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "END_OBJECT", "entityFile": "JsonToken.java"} --><!-- e7bfa171-173f-11ea-a3d5-333445793454 <=< ACCEPT -->The closing of a JSON object. Written using {@link JsonWriter#endObject}
        and read using {@link JsonReader#endObject}.<!-- ACCEPT >=> e7bfa171-173f-11ea-a3d5-333445793454 -->

# File: `GsonBuilder.java`

## Method: `public GsonBuilder disableInnerClassSerialization()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder disableInnerClassSerialization()", "entityFile": "GsonBuilder.java"} -->Configures Gson to exclude inner classes during serialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3

## Method: `public GsonBuilder setLongSerializationPolicy(LongSerializationPolicy serializationPolicy)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setLongSerializationPolicy(LongSerializationPolicy serializationPolicy)", "entityFile": "GsonBuilder.java"} -->Configures Gson to apply a specific serialization policy for {@code Long} and {@code long}
        objects.
        @param serializationPolicy the particular policy to use for serializing longs.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3

## Method: `public GsonBuilder setFieldNamingPolicy(FieldNamingPolicy namingConvention)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setFieldNamingPolicy(FieldNamingPolicy namingConvention)", "entityFile": "GsonBuilder.java"} --><!-- 0fe99b6c-1740-11ea-9564-333445793454 <=< ACCEPT -->Configures Gson to apply a specific naming policy to an object's field during serialization
        and deserialization.
        @param namingConvention the JSON field naming convention to use for serialization and
        deserialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern<!-- ACCEPT >=> 0fe99b6c-1740-11ea-9564-333445793454 -->

## Method: `public GsonBuilder setFieldNamingStrategy(FieldNamingStrategy fieldNamingStrategy)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setFieldNamingStrategy(FieldNamingStrategy fieldNamingStrategy)", "entityFile": "GsonBuilder.java"} --><!-- 0fe99b6c-1740-11ea-9564-333445793454 <=< ACCEPT -->Configures Gson to apply a specific naming policy strategy to an object's field during
        serialization and deserialization.
        @param fieldNamingStrategy the actual naming strategy to apply to the fields
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3<!-- ACCEPT >=> 0fe99b6c-1740-11ea-9564-333445793454 -->

## Method: `public GsonBuilder setExclusionStrategies(ExclusionStrategy... strategies)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setExclusionStrategies(ExclusionStrategy... strategies)", "entityFile": "GsonBuilder.java"} -->Configures Gson to apply a set of exclusion strategies during both serialization and
        deserialization. Each of the {@code strategies} will be applied as a disjunction rule.
        This means that if one of the {@code strategies} suggests that a field (or class) should be
        skipped then that field (or object) is skipped during serialization/deserialization.
        @param strategies the set of strategy object to apply during object (de)serialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.4

# File: `JsonToken.java`

## EnumConstant: `NAME`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "NAME", "entityFile": "JsonToken.java"} -->A JSON property name. Within objects, tokens alternate between names and
        their values. Written using {@link JsonWriter#name} and read using {@link
        JsonReader#nextName}

## EnumConstant: `STRING`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "STRING", "entityFile": "JsonToken.java"} -->A JSON string.

## EnumConstant: `NUMBER`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "NUMBER", "entityFile": "JsonToken.java"} -->A JSON number represented in this API by a Java {@code double}, {@code
        long}, or {@code int}.

## EnumConstant: `BOOLEAN`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "BOOLEAN", "entityFile": "JsonToken.java"} -->A JSON {@code true} or {@code false}.

## EnumConstant: `NULL`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "NULL", "entityFile": "JsonToken.java"} -->A JSON {@code null}.

## EnumConstant: `END_DOCUMENT`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "END_DOCUMENT", "entityFile": "JsonToken.java"} -->The end of the JSON stream. This sentinel value is returned by {@link
        JsonReader#peek()} to signal that the JSON-encoded value has no more
        tokens.

## Enum: `JsonToken`

        <!-- META {"entityType": "Enum", "entitySignature": "JsonToken", "entityFile": "JsonToken.java"} -->A structure, name or value type in a JSON-encoded string.
        @author Jesse Wilson
        @since 1.6

# File: `Excluder.java`

## Field: `delegate`

        <!-- META {"entityType": "Field", "entitySignature": "delegate", "entityFile": "Excluder.java"} -->The delegate is lazily created because it may not be needed, and creating it may fail.

# File: `GsonBuilder.java`

## Method: `public GsonBuilder addSerializationExclusionStrategy(ExclusionStrategy strategy)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder addSerializationExclusionStrategy(ExclusionStrategy strategy)", "entityFile": "GsonBuilder.java"} -->Configures Gson to apply the passed in exclusion strategy during serialization.
        If this method is invoked numerous times with different exclusion strategy objects
        then the exclusion strategies that were added will be applied as a disjunction rule.
        This means that if one of the added exclusion strategies suggests that a field (or
        class) should be skipped then that field (or object) is skipped during its
        serialization.
        @param strategy an exclusion strategy to apply during serialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.7

## Method: `public GsonBuilder addDeserializationExclusionStrategy(ExclusionStrategy strategy)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder addDeserializationExclusionStrategy(ExclusionStrategy strategy)", "entityFile": "GsonBuilder.java"} -->Configures Gson to apply the passed in exclusion strategy during deserialization.
        If this method is invoked numerous times with different exclusion strategy objects
        then the exclusion strategies that were added will be applied as a disjunction rule.
        This means that if one of the added exclusion strategies suggests that a field (or
        class) should be skipped then that field (or object) is skipped during its
        deserialization.
        @param strategy an exclusion strategy to apply during deserialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.7

## Method: `public GsonBuilder setPrettyPrinting()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setPrettyPrinting()", "entityFile": "GsonBuilder.java"} -->Configures Gson to output Json that fits in a page for pretty printing. This option only
        affects Json serialization.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern

## Method: `public GsonBuilder setLenient()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setLenient()", "entityFile": "GsonBuilder.java"} -->By default, Gson is strict and only accepts JSON as specified by
        <a href="http://www.ietf.org/rfc/rfc4627.txt">RFC 4627</a>. This option makes the parser
        liberal in what it accepts.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @see JsonReader#setLenient(boolean)

## Method: `public GsonBuilder disableHtmlEscaping()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder disableHtmlEscaping()", "entityFile": "GsonBuilder.java"} -->By default, Gson escapes HTML characters such as &lt; &gt; etc. Use this option to configure
        Gson to pass-through HTML characters as is.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3

## Method: `public GsonBuilder setDateFormat(String pattern)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setDateFormat(String pattern)", "entityFile": "GsonBuilder.java"} -->Configures Gson to serialize {@code Date} objects according to the pattern provided. You can
        call this method or {@link #setDateFormat(int)} multiple times, but only the last invocation
        will be used to decide the serialization format.
        <p>The date format will be used to serialize and deserialize {@link java.util.Date}, {@link
        java.sql.Timestamp} and {@link java.sql.Date}.
        <p>Note that this pattern must abide by the convention provided by {@code SimpleDateFormat}
        class. See the documentation in {@link java.text.SimpleDateFormat} for more information on
        valid date and time patterns.</p>
        @param pattern the pattern that dates will be serialized/deserialized to/from
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.2

# File: `Excluder.java`

## Class: `Excluder`

        <!-- META {"entityType": "Class", "entitySignature": "Excluder", "entityFile": "Excluder.java"} -->This class selects which fields and types to omit. It is configurable,
        supporting version attributes {@link Since} and {@link Until}, modifiers,
        synthetic fields, anonymous and local classes, inner classes, and fields with
        the {@link Expose} annotation.
        <p>This class is a type adapter factory; types that are excluded will be
        adapted to null. It may delegate to another type adapter if only one
        direction is excluded.
        @author Joel Leitch
        @author Jesse Wilson

# File: `JsonReaderInternalAccess.java`

## Method: `public abstract void promoteNameToValue(JsonReader reader) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract void promoteNameToValue(JsonReader reader) throws IOException", "entityFile": "JsonReaderInternalAccess.java"} -->Changes the type of the current property name token to a string value.

## Class: `JsonReaderInternalAccess`

        <!-- META {"entityType": "Class", "entitySignature": "JsonReaderInternalAccess", "entityFile": "JsonReaderInternalAccess.java"} -->Internal-only APIs of JsonReader available only to other classes in Gson.

# File: `LinkedHashTreeMap.java`

## Method: `public LinkedHashTreeMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public LinkedHashTreeMap()", "entityFile": "LinkedHashTreeMap.java"} -->Create a natural order, empty tree map whose keys must be mutually
        comparable and non-null.

## Method: `public LinkedHashTreeMap(Comparator<? super K> comparator)`

        <!-- META {"entityType": "Method", "entitySignature": "public LinkedHashTreeMap(Comparator<? super K> comparator)", "entityFile": "LinkedHashTreeMap.java"} -->Create a tree map ordered by {@code comparator}. This map's keys may only
        be null if {@code comparator} permits.
        @param comparator the comparator to order elements with, or {@code null} to
        use the natural ordering.

## Method: `Node<K, V> find(K key, boolean create)`

        <!-- META {"entityType": "Method", "entitySignature": "Node<K, V> find(K key, boolean create)", "entityFile": "LinkedHashTreeMap.java"} -->Returns the node at or adjacent to the given key, creating it if requested.
        @throws ClassCastException if {@code key} and the tree's keys aren't
        mutually comparable.

## Method: `Node<K, V> findByEntry(Entry<?, ?> entry)`

        <!-- META {"entityType": "Method", "entitySignature": "Node<K, V> findByEntry(Entry<?, ?> entry)", "entityFile": "LinkedHashTreeMap.java"} -->Returns this map's entry that has the same key and value as {@code
        entry}, or null if this map has no such entry.
        <p>This method uses the comparator for key equality rather than {@code
        equals}. If this map's comparator isn't consistent with equals (such as
        {@code String.CASE_INSENSITIVE_ORDER}), then {@code remove()} and {@code
        contains()} will violate the collections API.

## Method: `private static int secondaryHash(int h)`

        <!-- META {"entityType": "Method", "entitySignature": "private static int secondaryHash(int h)", "entityFile": "LinkedHashTreeMap.java"} -->Applies a supplemental hash function to a given hashCode, which defends
        against poor quality hash functions. This is critical because HashMap
        uses power-of-two length hash tables, that otherwise encounter collisions
        for hashCodes that do not differ in lower or upper bits.

## Method: `void removeInternal(Node<K, V> node, boolean unlink)`

        <!-- META {"entityType": "Method", "entitySignature": "void removeInternal(Node<K, V> node, boolean unlink)", "entityFile": "LinkedHashTreeMap.java"} -->Removes {@code node} from this tree, rearranging the tree's structure as
        necessary.
        @param unlink true to also unlink this node from the iteration linked list.

## Method: `private void rebalance(Node<K, V> unbalanced, boolean insert)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rebalance(Node<K, V> unbalanced, boolean insert)", "entityFile": "LinkedHashTreeMap.java"} -->Rebalances the tree by making any AVL rotations necessary between the
        newly-unbalanced node and the tree's root.
        @param insert true if the node was unbalanced by an insert; false if it
        was by a removal.

## Method: `private void rotateLeft(Node<K, V> root)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rotateLeft(Node<K, V> root)", "entityFile": "LinkedHashTreeMap.java"} -->Rotates the subtree so that its root's right child is the new root.

## Method: `private void rotateRight(Node<K, V> root)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rotateRight(Node<K, V> root)", "entityFile": "LinkedHashTreeMap.java"} -->Rotates the subtree so that its root's left child is the new root.

## Method: `Node()`

        <!-- META {"entityType": "Method", "entitySignature": "Node()", "entityFile": "LinkedHashTreeMap.java"} -->Create the header entry

## Method: `Node(Node<K, V> parent, K key, int hash, Node<K, V> next, Node<K, V> prev)`

        <!-- META {"entityType": "Method", "entitySignature": "Node(Node<K, V> parent, K key, int hash, Node<K, V> next, Node<K, V> prev)", "entityFile": "LinkedHashTreeMap.java"} -->Create a regular entry

## Method: `public Node<K, V> first()`

        <!-- META {"entityType": "Method", "entitySignature": "public Node<K, V> first()", "entityFile": "LinkedHashTreeMap.java"} -->Returns the first node in this subtree.

## Method: `public Node<K, V> last()`

        <!-- META {"entityType": "Method", "entitySignature": "public Node<K, V> last()", "entityFile": "LinkedHashTreeMap.java"} -->Returns the last node in this subtree.

## Method: `static Node<K, V>[] doubleCapacity(Node<K, V>[] oldTable)`

        <!-- META {"entityType": "Method", "entitySignature": "static Node<K, V>[] doubleCapacity(Node<K, V>[] oldTable)", "entityFile": "LinkedHashTreeMap.java"} -->Returns a new array containing the same nodes as {@code oldTable}, but with
        twice as many trees, each of (approximately) half the previous size.

## Field: `stackTop`

        <!-- META {"entityType": "Field", "entitySignature": "stackTop", "entityFile": "LinkedHashTreeMap.java"} -->This stack is a singly linked list, linked by the 'parent' field.

# File: `JsonWriter.java`

## Field: `out`

        <!-- META {"entityType": "Field", "entitySignature": "out", "entityFile": "JsonWriter.java"} -->The output data, containing at most one top-level array or object.

## Field: `indent`

        <!-- META {"entityType": "Field", "entitySignature": "indent", "entityFile": "JsonWriter.java"} -->A string containing a full set of spaces for a single level of
        indentation, or null for no pretty printing.

## Field: `separator`

        <!-- META {"entityType": "Field", "entitySignature": "separator", "entityFile": "JsonWriter.java"} -->The name/value separator; either ":" or ": ".

## Method: `public JsonWriter(Writer out)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter(Writer out)", "entityFile": "JsonWriter.java"} -->Creates a new instance that writes a JSON-encoded stream to {@code out}.
        For best performance, ensure {@link Writer} is buffered; wrapping in
        {@link java.io.BufferedWriter BufferedWriter} if necessary.

## Method: `public final void setIndent(String indent)`

        <!-- META {"entityType": "Method", "entitySignature": "public final void setIndent(String indent)", "entityFile": "JsonWriter.java"} -->Sets the indentation string to be repeated for each level of indentation
        in the encoded document. If {@code indent.isEmpty()} the encoded document
        will be compact. Otherwise the encoded document will be more
        human-readable.
        @param indent a string containing only whitespace.

## Method: `public final void setLenient(boolean lenient)`

        <!-- META {"entityType": "Method", "entitySignature": "public final void setLenient(boolean lenient)", "entityFile": "JsonWriter.java"} -->Configure this writer to relax its syntax rules. By default, this writer
        only emits well-formed JSON as specified by <a
        href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>. Setting the writer
        to lenient permits the following:
        <ul>
        <li>Top-level values of any type. With strict writing, the top-level
        value must be an object or an array.
        <li>Numbers may be {@link Double#isNaN() NaNs} or {@link
        Double#isInfinite() infinities}.
        </ul>

## Method: `public boolean isLenient()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isLenient()", "entityFile": "JsonWriter.java"} -->Returns true if this writer has relaxed syntax rules.

## Method: `public final void setHtmlSafe(boolean htmlSafe)`

        <!-- META {"entityType": "Method", "entitySignature": "public final void setHtmlSafe(boolean htmlSafe)", "entityFile": "JsonWriter.java"} -->Configure this writer to emit JSON that's safe for direct inclusion in HTML
        and XML documents. This escapes the HTML characters {@code <}, {@code >},
        {@code &} and {@code =} before writing them to the stream. Without this
        setting, your XML/HTML encoder should replace these characters with the
        corresponding escape sequences.

## Method: `public final boolean isHtmlSafe()`

        <!-- META {"entityType": "Method", "entitySignature": "public final boolean isHtmlSafe()", "entityFile": "JsonWriter.java"} -->Returns true if this writer writes JSON that's safe for inclusion in HTML
        and XML documents.

## Method: `public final void setSerializeNulls(boolean serializeNulls)`

        <!-- META {"entityType": "Method", "entitySignature": "public final void setSerializeNulls(boolean serializeNulls)", "entityFile": "JsonWriter.java"} -->Sets whether object members are serialized when their value is null.
        This has no impact on array elements. The default is true.

## Method: `public final boolean getSerializeNulls()`

        <!-- META {"entityType": "Method", "entitySignature": "public final boolean getSerializeNulls()", "entityFile": "JsonWriter.java"} -->Returns true if object members are serialized when their value is null.
        This has no impact on array elements. The default is true.

## Method: `public JsonWriter beginArray() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter beginArray() throws IOException", "entityFile": "JsonWriter.java"} -->Begins encoding a new array. Each call to this method must be paired with
        a call to {@link #endArray}.
        @return this writer.

## Method: `public JsonWriter endArray() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter endArray() throws IOException", "entityFile": "JsonWriter.java"} -->Ends encoding the current array.
        @return this writer.

## Method: `public JsonWriter beginObject() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter beginObject() throws IOException", "entityFile": "JsonWriter.java"} -->Begins encoding a new object. Each call to this method must be paired
        with a call to {@link #endObject}.
        @return this writer.

## Method: `public JsonWriter endObject() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter endObject() throws IOException", "entityFile": "JsonWriter.java"} -->Ends encoding the current object.
        @return this writer.

## Method: `private JsonWriter open(int empty, String openBracket) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private JsonWriter open(int empty, String openBracket) throws IOException", "entityFile": "JsonWriter.java"} -->Enters a new scope by appending any necessary whitespace and the given
        bracket.

# File: `GsonBuilder.java`

## Method: `public GsonBuilder setDateFormat(int style)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setDateFormat(int style)", "entityFile": "GsonBuilder.java"} --><!-- 40808baf-1740-11ea-b2ca-333445793454 <=< ACCEPT -->Configures Gson to to serialize {@code Date} objects according to the style value provided.
        You can call this method or {@link #setDateFormat(String)} multiple times, but only the last
        invocation will be used to decide the serialization format.
        <p>Note that this style value should be one of the predefined constants in the
        {@code DateFormat} class. See the documentation in {@link java.text.DateFormat} for more
        information on the valid style constants.</p>
        @param style the predefined date style that date objects will be serialized/deserialized
        to/from
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.2<!-- ACCEPT >=> 40808baf-1740-11ea-b2ca-333445793454 -->

## Method: `public GsonBuilder setDateFormat(int dateStyle, int timeStyle)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder setDateFormat(int dateStyle, int timeStyle)", "entityFile": "GsonBuilder.java"} --><!-- 40808baf-1740-11ea-b2ca-333445793454 <=< ACCEPT -->Configures Gson to to serialize {@code Date} objects according to the style value provided.
        You can call this method or {@link #setDateFormat(String)} multiple times, but only the last
        invocation will be used to decide the serialization format.
        <p>Note that this style value should be one of the predefined constants in the
        {@code DateFormat} class. See the documentation in {@link java.text.DateFormat} for more
        information on the valid style constants.</p>
        @param dateStyle the predefined date style that date objects will be serialized/deserialized
        to/from
        @param timeStyle the predefined style for the time portion of the date objects
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.2<!-- ACCEPT >=> 40808baf-1740-11ea-b2ca-333445793454 -->

## Method: `public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder registerTypeAdapter(Type type, Object typeAdapter)", "entityFile": "GsonBuilder.java"} -->Configures Gson for custom serialization or deserialization. This method combines the
        registration of an {@link TypeAdapter}, {@link InstanceCreator}, {@link JsonSerializer}, and a
        {@link JsonDeserializer}. It is best used when a single object {@code typeAdapter} implements
        all the required interfaces for custom serialization with Gson. If a type adapter was
        previously registered for the specified {@code type}, it is overwritten.
        <p>This registers the type specified and no other types: you must manually register related
        types! For example, applications registering {@code boolean.class} should also register {@code
        Boolean.class}.
        @param type the type definition for the type adapter being registered
        @param typeAdapter This object must implement at least one of the {@link TypeAdapter},
        {@link InstanceCreator}, {@link JsonSerializer}, and a {@link JsonDeserializer} interfaces.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern

## Method: `public GsonBuilder registerTypeAdapterFactory(TypeAdapterFactory factory)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder registerTypeAdapterFactory(TypeAdapterFactory factory)", "entityFile": "GsonBuilder.java"} -->Register a factory for type adapters. Registering a factory is useful when the type
        adapter needs to be configured based on the type of the field being processed. Gson
        is designed to handle a large number of factories, so you should consider registering
        them to be at par with registering an individual type adapter.
        @since 2.1

## Method: `public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder registerTypeHierarchyAdapter(Class<?> baseType, Object typeAdapter)", "entityFile": "GsonBuilder.java"} -->Configures Gson for custom serialization or deserialization for an inheritance type hierarchy.
        This method combines the registration of a {@link TypeAdapter}, {@link JsonSerializer} and
        a {@link JsonDeserializer}. If a type adapter was previously registered for the specified
        type hierarchy, it is overridden. If a type adapter is registered for a specific type in
        the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.
        @param baseType the class definition for the type adapter being registered for the base class
        or interface
        @param typeAdapter This object must implement at least one of {@link TypeAdapter},
        {@link JsonSerializer} or {@link JsonDeserializer} interfaces.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.7

# File: `LinkedHashTreeMap.java`

## Class: `AvlIterator`

        <!-- META {"entityType": "Class", "entitySignature": "AvlIterator", "entityFile": "LinkedHashTreeMap.java"} -->Walks an AVL tree in iteration order. Once a node has been returned, its
        left, right and parent links are <strong>no longer used</strong>. For this
        reason it is safe to transform these links as you walk a tree.
        <p><strong>Warning:</strong> this iterator is destructive. It clears the
        parent node of all nodes in the tree. It is an error to make a partial
        iteration of a tree.

## Field: `stack`

        <!-- META {"entityType": "Field", "entitySignature": "stack", "entityFile": "LinkedHashTreeMap.java"} -->This stack is a singly linked list, linked by the 'parent' field.

## Class: `AvlBuilder`

        <!-- META {"entityType": "Class", "entitySignature": "AvlBuilder", "entityFile": "LinkedHashTreeMap.java"} -->Builds AVL trees of a predetermined size by accepting nodes of increasing
        value. To use:
        <ol>
        <li>Call {@link #reset} to initialize the target size <i>size</i>.
        <li>Call {@link #add} <i>size</i> times with increasing values.
        <li>Call {@link #root} to get the root of the balanced tree.
        </ol>
        <p>The returned tree will satisfy the AVL constraint: for every node
        <i>N</i>, the height of <i>N.left</i> and <i>N.right</i> is different by at
        most 1. It accomplishes this by omitting deepest-level leaf nodes when
        building trees whose size isn't a power of 2 minus 1.
        <p>Unlike rebuilding a tree from scratch, this approach requires no value
        comparisons. Using this class to create a tree of size <i>S</i> is
        {@code O(S)}.

## Method: `private Object writeReplace() throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "private Object writeReplace() throws ObjectStreamException", "entityFile": "LinkedHashTreeMap.java"} -->If somebody is unlucky enough to have to serialize one of these, serialize
        it as a LinkedHashMap so that they won't need Gson on the other side to
        deserialize it. Using serialization defeats our DoS defence, so most apps
        shouldn't use it.

## Class: `LinkedHashTreeMap`

        <!-- META {"entityType": "Class", "entitySignature": "LinkedHashTreeMap", "entityFile": "LinkedHashTreeMap.java"} -->A map of comparable keys to values. Unlike {@code TreeMap}, this class uses
        insertion order for iteration order. Comparison order is only used as an
        optimization for efficient insertion and removal.
        <p>This implementation was derived from Android 4.1's TreeMap and
        LinkedHashMap classes.

# File: `ReflectiveTypeAdapterFactory.java`

## Method: `private List<String> getFieldNames(Field f)`

        <!-- META {"entityType": "Method", "entitySignature": "private List<String> getFieldNames(Field f)", "entityFile": "ReflectiveTypeAdapterFactory.java"} -->first element holds the default name

## Method: `static List<String> getFieldName(FieldNamingStrategy fieldNamingPolicy, Field f)`

        <!-- META {"entityType": "Method", "entitySignature": "static List<String> getFieldName(FieldNamingStrategy fieldNamingPolicy, Field f)", "entityFile": "ReflectiveTypeAdapterFactory.java"} -->first element holds the default name

## Class: `ReflectiveTypeAdapterFactory`

        <!-- META {"entityType": "Class", "entitySignature": "ReflectiveTypeAdapterFactory", "entityFile": "ReflectiveTypeAdapterFactory.java"} -->Type adapter that reflects over the fields and methods of a class.

# File: `JsonWriter.java`

## Method: `private JsonWriter close(int empty, int nonempty, String closeBracket) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private JsonWriter close(int empty, int nonempty, String closeBracket) throws IOException", "entityFile": "JsonWriter.java"} -->Closes the current scope by appending any necessary whitespace and the
        given bracket.

## Method: `private int peek()`

        <!-- META {"entityType": "Method", "entitySignature": "private int peek()", "entityFile": "JsonWriter.java"} -->Returns the value on the top of the stack.

## Method: `private void replaceTop(int topOfStack)`

        <!-- META {"entityType": "Method", "entitySignature": "private void replaceTop(int topOfStack)", "entityFile": "JsonWriter.java"} -->Replace the value on the top of the stack with the given value.

## Method: `public JsonWriter name(String name) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter name(String name) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes the property name.
        @param name the name of the forthcoming value. May not be null.
        @return this writer.

## Method: `public JsonWriter value(String value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter value(String value) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code value}.
        @param value the literal string value, or null to encode a null literal.
        @return this writer.

## Method: `public JsonWriter jsonValue(String value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter jsonValue(String value) throws IOException", "entityFile": "JsonWriter.java"} -->Writes {@code value} directly to the writer without quoting or
        escaping.
        @param value the literal string value, or null to encode a null literal.
        @return this writer.

## Method: `public JsonWriter nullValue() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter nullValue() throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code null}.
        @return this writer.

## Method: `public JsonWriter value(boolean value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter value(boolean value) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code value}.
        @return this writer.

## Method: `public JsonWriter value(double value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter value(double value) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code value}.
        @param value a finite value. May not be {@link Double#isNaN() NaNs} or
        {@link Double#isInfinite() infinities}.
        @return this writer.

## Method: `public JsonWriter value(long value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter value(long value) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code value}.
        @return this writer.

## Method: `public JsonWriter value(Number value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonWriter value(Number value) throws IOException", "entityFile": "JsonWriter.java"} -->Encodes {@code value}.
        @param value a finite value. May not be {@link Double#isNaN() NaNs} or
        {@link Double#isInfinite() infinities}.
        @return this writer.

## Method: `public void flush() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void flush() throws IOException", "entityFile": "JsonWriter.java"} -->Ensures all buffered data is written to the underlying {@link Writer}
        and flushes that writer.

## Method: `public void close() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public void close() throws IOException", "entityFile": "JsonWriter.java"} -->Flushes and closes this writer and the underlying {@link Writer}.
        @throws IOException if the JSON document is incomplete.

## Method: `private void beforeName() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private void beforeName() throws IOException", "entityFile": "JsonWriter.java"} -->Inserts any necessary separators and whitespace before a name. Also
        adjusts the stack to expect the name's value.

## Method: `private void beforeValue() throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "private void beforeValue() throws IOException", "entityFile": "JsonWriter.java"} -->Inserts any necessary separators and whitespace before a literal value,
        inline array, or inline object. Also adjusts the stack to expect either a
        closing bracket or another element.

## Class: `JsonWriter`

        <!-- META {"entityType": "Class", "entitySignature": "JsonWriter", "entityFile": "JsonWriter.java"} -->Writes a JSON (<a href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>)
        encoded value to a stream, one token at a time. The stream includes both
        literal values (strings, numbers, booleans and nulls) as well as the begin
        and end delimiters of objects and arrays.
        <h3>Encoding JSON</h3>
        To encode your data as JSON, create a new {@code JsonWriter}. Each JSON
        document must contain one top-level array or object. Call methods on the
        writer as you walk the structure's contents, nesting arrays and objects as
        necessary:
        <ul>
        <li>To write <strong>arrays</strong>, first call {@link #beginArray()}.
        Write each of the array's elements with the appropriate {@link #value}
        methods or by nesting other arrays and objects. Finally close the array
        using {@link #endArray()}.
        <li>To write <strong>objects</strong>, first call {@link #beginObject()}.
        Write each of the object's properties by alternating calls to
        {@link #name} with the property's value. Write property values with the
        appropriate {@link #value} method or by nesting other objects or arrays.
        Finally close the object using {@link #endObject()}.
        </ul>
        <h3>Example</h3>
        Suppose we'd like to encode a stream of messages such as the following: <pre> {@code
        [
        {
        "id": 912345678901,
        "text": "How do I stream JSON in Java?",
        "geo": null,
        "user": {
        "name": "json_newb",
        "followers_count": 41
        }
        },
        {
        "id": 912345678902,
        "text": "@json_newb just use JsonWriter!",
        "geo": [50.454722, -104.606667],
        "user": {
        "name": "jesse",
        "followers_count": 2
        }
        }
        ]}</pre>
        This code encodes the above structure: <pre>   {@code
        public void writeJsonStream(OutputStream out, List<Message> messages) throws IOException {
        JsonWriter writer = new JsonWriter(new OutputStreamWriter(out, "UTF-8"));
        writer.setIndent("    ");
        writeMessagesArray(writer, messages);
        writer.close();
        }
        public void writeMessagesArray(JsonWriter writer, List<Message> messages) throws IOException {
        writer.beginArray();
        for (Message message : messages) {
        writeMessage(writer, message);
        }
        writer.endArray();
        }
        public void writeMessage(JsonWriter writer, Message message) throws IOException {
        writer.beginObject();
        writer.name("id").value(message.getId());
        writer.name("text").value(message.getText());
        if (message.getGeo() != null) {
        writer.name("geo");
        writeDoublesArray(writer, message.getGeo());
        } else {
        writer.name("geo").nullValue();
        }
        writer.name("user");
        writeUser(writer, message.getUser());
        writer.endObject();
        }
        public void writeUser(JsonWriter writer, User user) throws IOException {
        writer.beginObject();
        writer.name("name").value(user.getName());
        writer.name("followers_count").value(user.getFollowersCount());
        writer.endObject();
        }
        public void writeDoublesArray(JsonWriter writer, List<Double> doubles) throws IOException {
        writer.beginArray();
        for (Double value : doubles) {
        writer.value(value);
        }
        writer.endArray();
        }}</pre>
        <p>Each {@code JsonWriter} may be used to write a single JSON stream.
        Instances of this class are not thread safe. Calls that would result in a
        malformed JSON string will fail with an {@link IllegalStateException}.
        @author Jesse Wilson
        @since 1.6

# File: `SqlDateTypeAdapter.java`

## Class: `SqlDateTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "SqlDateTypeAdapter", "entityFile": "SqlDateTypeAdapter.java"} --><!-- 737161d5-1740-11ea-b3f9-333445793454 <=< ACCEPT -->Adapter for java.sql.Date. Although this class appears stateless, it is not.
        DateFormat captures its time zone and locale when it is created, which gives
        this class state. DateFormat isn't thread safe either, so this class has
        to synchronize its read and write methods.<!-- ACCEPT >=> 737161d5-1740-11ea-b3f9-333445793454 -->

# File: `MalformedJsonException.java`

## Class: `MalformedJsonException`

        <!-- META {"entityType": "Class", "entitySignature": "MalformedJsonException", "entityFile": "MalformedJsonException.java"} -->Thrown when a reader encounters malformed JSON. Some syntax errors can be
        ignored by calling {@link JsonReader#setLenient(boolean)}.

# File: `GsonBuilder.java`

## Method: `public GsonBuilder serializeSpecialFloatingPointValues()`

        <!-- META {"entityType": "Method", "entitySignature": "public GsonBuilder serializeSpecialFloatingPointValues()", "entityFile": "GsonBuilder.java"} -->Section 2.4 of <a href="http://www.ietf.org/rfc/rfc4627.txt">JSON specification</a> disallows
        special double values (NaN, Infinity, -Infinity). However,
        <a href="http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf">Javascript
        specification</a> (see section 4.3.20, 4.3.22, 4.3.23) allows these values as valid Javascript
        values. Moreover, most JavaScript engines will accept these special values in JSON without
        problem. So, at a practical level, it makes sense to accept these values as valid JSON even
        though JSON specification disallows them.
        <p>Gson always accepts these special values during deserialization. However, it outputs
        strictly compliant JSON. Hence, if it encounters a float value {@link Float#NaN},
        {@link Float#POSITIVE_INFINITY}, {@link Float#NEGATIVE_INFINITY}, or a double value
        {@link Double#NaN}, {@link Double#POSITIVE_INFINITY}, {@link Double#NEGATIVE_INFINITY}, it
        will throw an {@link IllegalArgumentException}. This method provides a way to override the
        default behavior when you know that the JSON receiver will be able to handle these special
        values.
        @return a reference to this {@code GsonBuilder} object to fulfill the "Builder" pattern
        @since 1.3

## Method: `public Gson create()`

        <!-- META {"entityType": "Method", "entitySignature": "public Gson create()", "entityFile": "GsonBuilder.java"} -->Creates a {@link Gson} instance based on the current configuration. This method is free of
        side-effects to this {@code GsonBuilder} instance and hence can be called multiple times.
        @return an instance of Gson configured with the options currently set in this builder

## Class: `GsonBuilder`

        <!-- META {"entityType": "Class", "entitySignature": "GsonBuilder", "entityFile": "GsonBuilder.java"} --><p>Use this builder to construct a {@link Gson} instance when you need to set configuration
        options other than the default. For {@link Gson} with default configuration, it is simpler to
        use {@code new Gson()}. {@code GsonBuilder} is best used by creating it, and then invoking its
        various configuration methods, and finally calling create.</p>
        <p>The following is an example shows how to use the {@code GsonBuilder} to construct a Gson
        instance:
        <pre>
        Gson gson = new GsonBuilder()
        .registerTypeAdapter(Id.class, new IdTypeAdapter())
        .enableComplexMapKeySerialization()
        .serializeNulls()
        .setDateFormat(DateFormat.LONG)
        .setFieldNamingPolicy(FieldNamingPolicy.UPPER_CAMEL_CASE)
        .setPrettyPrinting()
        .setVersion(1.0)
        .create();
        </pre></p>
        <p>NOTES:
        <ul>
        <li> the order of invocation of configuration methods does not matter.</li>
        <li> The default serialization of {@link Date} and its subclasses in Gson does
        not contain time-zone information. So, if you are using date/time instances,
        use {@code GsonBuilder} and its {@code setDateFormat} methods.</li>
        </ul>
        </p>
        @author Inderjeet Singh
        @author Joel Leitch
        @author Jesse Wilson

# File: `InstanceCreator.java`

## Method: `public T createInstance(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public T createInstance(Type type)", "entityFile": "InstanceCreator.java"} -->Gson invokes this call-back method during deserialization to create an instance of the
        specified type. The fields of the returned instance are overwritten with the data present
        in the Json. Since the prior contents of the object are destroyed and overwritten, do not
        return an instance that is useful elsewhere. In particular, do not return a common instance,
        always use {@code new} to create a new instance.
        @param type the parameterized T represented as a {@link Type}.
        @return a default object instance of type T.

## Interface: `InstanceCreator`

        <!-- META {"entityType": "Interface", "entitySignature": "InstanceCreator", "entityFile": "InstanceCreator.java"} -->This interface is implemented to create instances of a class that does not define a no-args
        constructor. If you can modify the class, you should instead add a private, or public
        no-args constructor. However, that is not possible for library classes, such as JDK classes, or
        a third-party library that you do not have source-code of. In such cases, you should define an
        instance creator for the class. Implementations of this interface should be registered with
        {@link GsonBuilder#registerTypeAdapter(Type, Object)} method before Gson will be able to use
        them.
        <p>Let us look at an example where defining an InstanceCreator might be useful. The
        {@code Id} class defined below does not have a default no-args constructor.</p>
        <pre>
        public class Id&lt;T&gt; {
        private final Class&lt;T&gt; clazz;
        private final long value;
        public Id(Class&lt;T&gt; clazz, long value) {
        this.clazz = clazz;
        this.value = value;
        }
        }
        </pre>
        <p>If Gson encounters an object of type {@code Id} during deserialization, it will throw an
        exception. The easiest way to solve this problem will be to add a (public or private) no-args
        constructor as follows:</p>
        <pre>
        private Id() {
        this(Object.class, 0L);
        }
        </pre>
        <p>However, let us assume that the developer does not have access to the source-code of the
        {@code Id} class, or does not want to define a no-args constructor for it. The developer
        can solve this problem by defining an {@code InstanceCreator} for {@code Id}:</p>
        <pre>
        class IdInstanceCreator implements InstanceCreator&lt;Id&gt; {
        public Id createInstance(Type type) {
        return new Id(Object.class, 0L);
        }
        }
        </pre>
        <p>Note that it does not matter what the fields of the created instance contain since Gson will
        overwrite them with the deserialized values specified in Json. You should also ensure that a
        <i>new</i> object is returned, not a common object since its fields will be overwritten.
        The developer will need to register {@code IdInstanceCreator} with Gson as follows:</p>
        <pre>
        Gson gson = new GsonBuilder().registerTypeAdapter(Id.class, new IdInstanceCreator()).create();
        </pre>
        @param <T> the type of object that will be created by this implementation.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TimeTypeAdapter.java`

## Class: `TimeTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "TimeTypeAdapter", "entityFile": "TimeTypeAdapter.java"} --><!-- 737161d5-1740-11ea-b3f9-333445793454 <=< ACCEPT -->Adapter for Time. Although this class appears stateless, it is not.
        DateFormat captures its time zone and locale when it is created, which gives
        this class state. DateFormat isn't thread safe either, so this class has
        to synchronize its read and write methods.<!-- ACCEPT >=> 737161d5-1740-11ea-b3f9-333445793454 -->

# File: `$Gson$Preconditions.java`

## Class: `$Gson$Preconditions`

        <!-- META {"entityType": "Class", "entitySignature": "$Gson$Preconditions", "entityFile": "$Gson$Preconditions.java"} -->A simple utility class used to check method Preconditions.
        <pre>
        public long divideBy(long value) {
        Preconditions.checkArgument(value != 0);
        return this.value / value;
        }
        </pre>
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TypeAdapterRuntimeTypeWrapper.java`

## Method: `private Type getRuntimeTypeIfMoreSpecific(Type type, Object value)`

        <!-- META {"entityType": "Method", "entitySignature": "private Type getRuntimeTypeIfMoreSpecific(Type type, Object value)", "entityFile": "TypeAdapterRuntimeTypeWrapper.java"} -->Finds a compatible runtime type if it is more specific

# File: `Since.java`

## AnnotationMember: `value`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "value", "entityFile": "Since.java"} -->the value indicating a version number since this member
        or type has been present.

## Annotation: `Since`

        <!-- META {"entityType": "Annotation", "entitySignature": "Since", "entityFile": "Since.java"} -->An annotation that indicates the version number since a member or a type has been present.
        This annotation is useful to manage versioning of your Json classes for a web-service.
        <p>
        This annotation has no effect unless you build {@link com.google.gson.Gson} with a
        {@link com.google.gson.GsonBuilder} and invoke
        {@link com.google.gson.GsonBuilder#setVersion(double)} method.
        <p>Here is an example of how this annotation is meant to be used:</p>
        <pre>
        public class User {
        private String firstName;
        private String lastName;
        &#64Since(1.0) private String emailAddress;
        &#64Since(1.0) private String password;
        &#64Since(1.1) private Address address;
        }
        </pre>
        <p>If you created Gson with {@code new Gson()}, the {@code toJson()} and {@code fromJson()}
        methods will use all the fields for serialization and deserialization. However, if you created
        Gson with {@code Gson gson = new GsonBuilder().setVersion(1.0).create()} then the
        {@code toJson()} and {@code fromJson()} methods of Gson will exclude the {@code address} field
        since it's version number is set to {@code 1.1}.</p>
        @author Inderjeet Singh
        @author Joel Leitch

# File: `Until.java`

## AnnotationMember: `value`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "value", "entityFile": "Until.java"} -->the value indicating a version number until this member
        or type should be ignored.

# File: `LinkedTreeMap.java`

## Method: `public LinkedTreeMap()`

        <!-- META {"entityType": "Method", "entitySignature": "public LinkedTreeMap()", "entityFile": "LinkedTreeMap.java"} -->Create a natural order, empty tree map whose keys must be mutually
        comparable and non-null.

# File: `Until.java`

## Annotation: `Until`

        <!-- META {"entityType": "Annotation", "entitySignature": "Until", "entityFile": "Until.java"} -->An annotation that indicates the version number until a member or a type should be present.
        Basically, if Gson is created with a version number that exceeds the value stored in the
        {@code Until} annotation then the field will be ignored from the JSON output.  This annotation
        is useful to manage versioning of your JSON classes for a web-service.
        <p>
        This annotation has no effect unless you build {@link com.google.gson.Gson} with a
        {@link com.google.gson.GsonBuilder} and invoke
        {@link com.google.gson.GsonBuilder#setVersion(double)} method.
        <p>Here is an example of how this annotation is meant to be used:</p>
        <pre>
        public class User {
        private String firstName;
        private String lastName;
        &#64Until(1.1) private String emailAddress;
        &#64Until(1.1) private String password;
        }
        </pre>
        <p>If you created Gson with {@code new Gson()}, the {@code toJson()} and {@code fromJson()}
        methods will use all the fields for serialization and deserialization. However, if you created
        Gson with {@code Gson gson = new GsonBuilder().setVersion(1.2).create()} then the
        {@code toJson()} and {@code fromJson()} methods of Gson will exclude the {@code emailAddress}
        and {@code password} fields from the example above, because the version number passed to the
        GsonBuilder, {@code 1.2}, exceeds the version number set on the {@code Until} annotation,
        {@code 1.1}, for those fields.
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.3

# File: `TreeTypeAdapter.java`

## Field: `delegate`

        <!-- META {"entityType": "Field", "entitySignature": "delegate", "entityFile": "TreeTypeAdapter.java"} -->The delegate is lazily created because it may not be needed, and creating it may fail.

# File: `LinkedTreeMap.java`

## Method: `public LinkedTreeMap(Comparator<? super K> comparator)`

        <!-- META {"entityType": "Method", "entitySignature": "public LinkedTreeMap(Comparator<? super K> comparator)", "entityFile": "LinkedTreeMap.java"} -->Create a tree map ordered by {@code comparator}. This map's keys may only
        be null if {@code comparator} permits.
        @param comparator the comparator to order elements with, or {@code null} to
        use the natural ordering.

# File: `TreeTypeAdapter.java`

## Method: `public static TypeAdapterFactory newFactory(TypeToken<?> exactType, Object typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeAdapterFactory newFactory(TypeToken<?> exactType, Object typeAdapter)", "entityFile": "TreeTypeAdapter.java"} -->Returns a new factory that will match each type against {@code exactType}.

## Method: `public static TypeAdapterFactory newFactoryWithMatchRawType(TypeToken<?> exactType, Object typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeAdapterFactory newFactoryWithMatchRawType(TypeToken<?> exactType, Object typeAdapter)", "entityFile": "TreeTypeAdapter.java"} -->Returns a new factory that will match each type and its raw type against
        {@code exactType}.

# File: `LinkedTreeMap.java`

## Method: `Node<K, V> find(K key, boolean create)`

        <!-- META {"entityType": "Method", "entitySignature": "Node<K, V> find(K key, boolean create)", "entityFile": "LinkedTreeMap.java"} -->Returns the node at or adjacent to the given key, creating it if requested.
        @throws ClassCastException if {@code key} and the tree's keys aren't
        mutually comparable.

## Method: `Node<K, V> findByEntry(Entry<?, ?> entry)`

        <!-- META {"entityType": "Method", "entitySignature": "Node<K, V> findByEntry(Entry<?, ?> entry)", "entityFile": "LinkedTreeMap.java"} -->Returns this map's entry that has the same key and value as {@code
        entry}, or null if this map has no such entry.
        <p>This method uses the comparator for key equality rather than {@code
        equals}. If this map's comparator isn't consistent with equals (such as
        {@code String.CASE_INSENSITIVE_ORDER}), then {@code remove()} and {@code
        contains()} will violate the collections API.

## Method: `void removeInternal(Node<K, V> node, boolean unlink)`

        <!-- META {"entityType": "Method", "entitySignature": "void removeInternal(Node<K, V> node, boolean unlink)", "entityFile": "LinkedTreeMap.java"} -->Removes {@code node} from this tree, rearranging the tree's structure as
        necessary.
        @param unlink true to also unlink this node from the iteration linked list.

## Method: `private void rebalance(Node<K, V> unbalanced, boolean insert)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rebalance(Node<K, V> unbalanced, boolean insert)", "entityFile": "LinkedTreeMap.java"} -->Rebalances the tree by making any AVL rotations necessary between the
        newly-unbalanced node and the tree's root.
        @param insert true if the node was unbalanced by an insert; false if it
        was by a removal.

## Method: `private void rotateLeft(Node<K, V> root)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rotateLeft(Node<K, V> root)", "entityFile": "LinkedTreeMap.java"} -->Rotates the subtree so that its root's right child is the new root.

## Method: `private void rotateRight(Node<K, V> root)`

        <!-- META {"entityType": "Method", "entitySignature": "private void rotateRight(Node<K, V> root)", "entityFile": "LinkedTreeMap.java"} -->Rotates the subtree so that its root's left child is the new root.

## Method: `Node()`

        <!-- META {"entityType": "Method", "entitySignature": "Node()", "entityFile": "LinkedTreeMap.java"} -->Create the header entry

## Method: `Node(Node<K, V> parent, K key, Node<K, V> next, Node<K, V> prev)`

        <!-- META {"entityType": "Method", "entitySignature": "Node(Node<K, V> parent, K key, Node<K, V> next, Node<K, V> prev)", "entityFile": "LinkedTreeMap.java"} -->Create a regular entry

## Method: `public Node<K, V> first()`

        <!-- META {"entityType": "Method", "entitySignature": "public Node<K, V> first()", "entityFile": "LinkedTreeMap.java"} -->Returns the first node in this subtree.

## Method: `public Node<K, V> last()`

        <!-- META {"entityType": "Method", "entitySignature": "public Node<K, V> last()", "entityFile": "LinkedTreeMap.java"} -->Returns the last node in this subtree.

## Method: `private Object writeReplace() throws ObjectStreamException`

        <!-- META {"entityType": "Method", "entitySignature": "private Object writeReplace() throws ObjectStreamException", "entityFile": "LinkedTreeMap.java"} -->If somebody is unlucky enough to have to serialize one of these, serialize
        it as a LinkedHashMap so that they won't need Gson on the other side to
        deserialize it. Using serialization defeats our DoS defence, so most apps
        shouldn't use it.

## Class: `LinkedTreeMap`

        <!-- META {"entityType": "Class", "entitySignature": "LinkedTreeMap", "entityFile": "LinkedTreeMap.java"} -->A map of comparable keys to values. Unlike {@code TreeMap}, this class uses
        insertion order for iteration order. Comparison order is only used as an
        optimization for efficient insertion and removal.
        <p>This implementation was derived from Android 4.1's TreeMap class.

# File: `TreeTypeAdapter.java`

## Method: `public static TypeAdapterFactory newTypeHierarchyFactory(Class<?> hierarchyType, Object typeAdapter)`

        <!-- META {"entityType": "Method", "entitySignature": "public static TypeAdapterFactory newTypeHierarchyFactory(Class<?> hierarchyType, Object typeAdapter)", "entityFile": "TreeTypeAdapter.java"} -->Returns a new factory that will match each type's raw type for assignability
        to {@code hierarchyType}.

# File: `DefaultDateTypeAdapter.java`

## Class: `DefaultDateTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "DefaultDateTypeAdapter", "entityFile": "DefaultDateTypeAdapter.java"} -->This type adapter supports three subclasses of date: Date, Timestamp, and
        java.sql.Date.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TreeTypeAdapter.java`

## Class: `TreeTypeAdapter`

        <!-- META {"entityType": "Class", "entitySignature": "TreeTypeAdapter", "entityFile": "TreeTypeAdapter.java"} -->Adapts a Gson 1.x tree-style adapter as a streaming TypeAdapter. Since the
        tree adapter may be serialization-only or deserialization-only, this class
        has a facility to lookup a delegate type adapter on demand.

# File: `ObjectConstructor.java`

## Method: `public T construct()`

        <!-- META {"entityType": "Method", "entitySignature": "public T construct()", "entityFile": "ObjectConstructor.java"} -->Returns a new instance.

## Interface: `ObjectConstructor`

        <!-- META {"entityType": "Interface", "entitySignature": "ObjectConstructor", "entityFile": "ObjectConstructor.java"} -->Defines a generic object construction factory.  The purpose of this class
        is to construct a default instance of a class that can be used for object
        navigation while deserialization from its JSON representation.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `ExclusionStrategy.java`

## Method: `public boolean shouldSkipField(FieldAttributes f)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean shouldSkipField(FieldAttributes f)", "entityFile": "ExclusionStrategy.java"} -->@param f the field object that is under test
        @return true if the field should be ignored; otherwise false

## Method: `public boolean shouldSkipClass(Class<?> clazz)`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean shouldSkipClass(Class<?> clazz)", "entityFile": "ExclusionStrategy.java"} -->@param clazz the class object that is under test
        @return true if the class should be ignored; otherwise false

## Interface: `ExclusionStrategy`

        <!-- META {"entityType": "Interface", "entitySignature": "ExclusionStrategy", "entityFile": "ExclusionStrategy.java"} -->A strategy (or policy) definition that is used to decide whether or not a field or top-level
        class should be serialized or deserialized as part of the JSON output/input. For serialization,
        if the {@link #shouldSkipClass(Class)} method returns true then that class or field type
        will not be part of the JSON output.  For deserialization, if {@link #shouldSkipClass(Class)}
        returns true, then it will not be set as part of the Java object structure.
        <p>The following are a few examples that shows how you can use this exclusion mechanism.
        <p><strong>Exclude fields and objects based on a particular class type:</strong>
        <pre class="code">
        private static class SpecificClassExclusionStrategy implements ExclusionStrategy {
        private final Class&lt;?&gt; excludedThisClass;
        public SpecificClassExclusionStrategy(Class&lt;?&gt; excludedThisClass) {
        this.excludedThisClass = excludedThisClass;
        }
        public boolean shouldSkipClass(Class&lt;?&gt; clazz) {
        return excludedThisClass.equals(clazz);
        }
        public boolean shouldSkipField(FieldAttributes f) {
        return excludedThisClass.equals(f.getDeclaredClass());
        }
        }
        </pre>
        <p><strong>Excludes fields and objects based on a particular annotation:</strong>
        <pre class="code">
        public &#64interface FooAnnotation {
        // some implementation here
        }
        // Excludes any field (or class) that is tagged with an "&#64FooAnnotation"
        private static class FooAnnotationExclusionStrategy implements ExclusionStrategy {
        public boolean shouldSkipClass(Class&lt;?&gt; clazz) {
        return clazz.getAnnotation(FooAnnotation.class) != null;
        }
        public boolean shouldSkipField(FieldAttributes f) {
        return f.getAnnotation(FooAnnotation.class) != null;
        }
        }
        </pre>
        <p>Now if you want to configure {@code Gson} to use a user defined exclusion strategy, then
        the {@code GsonBuilder} is required. The following is an example of how you can use the
        {@code GsonBuilder} to configure Gson to use one of the above sample:
        <pre class="code">
        ExclusionStrategy excludeStrings = new UserDefinedExclusionStrategy(String.class);
        Gson gson = new GsonBuilder()
        .setExclusionStrategies(excludeStrings)
        .create();
        </pre>
        <p>For certain model classes, you may only want to serialize a field, but exclude it for
        deserialization. To do that, you can write an {@code ExclusionStrategy} as per normal;
        however, you would register it with the
        {@link GsonBuilder#addDeserializationExclusionStrategy(ExclusionStrategy)} method.
        For example:
        <pre class="code">
        ExclusionStrategy excludeStrings = new UserDefinedExclusionStrategy(String.class);
        Gson gson = new GsonBuilder()
        .addDeserializationExclusionStrategy(excludeStrings)
        .create();
        </pre>
        @author Inderjeet Singh
        @author Joel Leitch
        @see GsonBuilder#setExclusionStrategies(ExclusionStrategy...)
        @see GsonBuilder#addDeserializationExclusionStrategy(ExclusionStrategy)
        @see GsonBuilder#addSerializationExclusionStrategy(ExclusionStrategy)
        @since 1.4

# File: `TypeAdapter.java`

## Method: `public abstract void write(JsonWriter out, T value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract void write(JsonWriter out, T value) throws IOException", "entityFile": "TypeAdapter.java"} -->Writes one JSON value (an array, object, string, number, boolean or null)
        for {@code value}.
        @param value the Java object to write. May be null.

## Method: `public final void toJson(Writer out, T value) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public final void toJson(Writer out, T value) throws IOException", "entityFile": "TypeAdapter.java"} -->Converts {@code value} to a JSON document and writes it to {@code out}.
        Unlike Gson's similar {@link Gson#toJson(JsonElement, Appendable) toJson}
        method, this write is strict. Create a {@link
        JsonWriter#setLenient(boolean) lenient} {@code JsonWriter} and call
        {@link #write(com.google.gson.stream.JsonWriter, Object)} for lenient
        writing.
        @param value the Java object to convert. May be null.
        @since 2.2

# File: `Expose.java`

## AnnotationMember: `serialize`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "serialize", "entityFile": "Expose.java"} -->If {@code true}, the field marked with this annotation is written out in the JSON while
        serializing. If {@code false}, the field marked with this annotation is skipped from the
        serialized output. Defaults to {@code true}.
        @since 1.4

## AnnotationMember: `deserialize`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "deserialize", "entityFile": "Expose.java"} -->If {@code true}, the field marked with this annotation is deserialized from the JSON.
        If {@code false}, the field marked with this annotation is skipped during deserialization.
        Defaults to {@code true}.
        @since 1.4

## Annotation: `Expose`

        <!-- META {"entityType": "Annotation", "entitySignature": "Expose", "entityFile": "Expose.java"} -->An annotation that indicates this member should be exposed for JSON
        serialization or deserialization.
        <p>This annotation has no effect unless you build {@link com.google.gson.Gson}
        with a {@link com.google.gson.GsonBuilder} and invoke
        {@link com.google.gson.GsonBuilder#excludeFieldsWithoutExposeAnnotation()}
        method.</p>
        <p>Here is an example of how this annotation is meant to be used:
        <p><pre>
        public class User {
        &#64Expose private String firstName;
        &#64Expose(serialize = false) private String lastName;
        &#64Expose (serialize = false, deserialize = false) private String emailAddress;
        private String password;
        }
        </pre></p>
        If you created Gson with {@code new Gson()}, the {@code toJson()} and {@code fromJson()}
        methods will use the {@code password} field along-with {@code firstName}, {@code lastName},
        and {@code emailAddress} for serialization and deserialization. However, if you created Gson
        with {@code Gson gson = new GsonBuilder().excludeFieldsWithoutExposeAnnotation().create()}
        then the {@code toJson()} and {@code fromJson()} methods of Gson will exclude the
        {@code password} field. This is because the {@code password} field is not marked with the
        {@code @Expose} annotation. Gson will also exclude {@code lastName} and {@code emailAddress}
        from serialization since {@code serialize} is set to {@code false}. Similarly, Gson will
        exclude {@code emailAddress} from deserialization since {@code deserialize} is set to false.
        <p>Note that another way to achieve the same effect would have been to just mark the
        {@code password} field as {@code transient}, and Gson would have excluded it even with default
        settings. The {@code @Expose} annotation is useful in a style of programming where you want to
        explicitly specify all fields that should get considered for serialization or deserialization.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `$Gson$Types.java`

## Method: `public static ParameterizedType newParameterizedTypeWithOwner(Type ownerType, Type rawType, Type... typeArguments)`

        <!-- META {"entityType": "Method", "entitySignature": "public static ParameterizedType newParameterizedTypeWithOwner(Type ownerType, Type rawType, Type... typeArguments)", "entityFile": "$Gson$Types.java"} -->Returns a new parameterized type, applying {@code typeArguments} to
        {@code rawType} and enclosed by {@code ownerType}.
        @return a {@link java.io.Serializable serializable} parameterized type.

## Method: `public static GenericArrayType arrayOf(Type componentType)`

        <!-- META {"entityType": "Method", "entitySignature": "public static GenericArrayType arrayOf(Type componentType)", "entityFile": "$Gson$Types.java"} -->Returns an array type whose elements are all instances of
        {@code componentType}.
        @return a {@link java.io.Serializable serializable} generic array type.

# File: `JsonAdapter.java`

## AnnotationMember: `value`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "value", "entityFile": "JsonAdapter.java"} -->Either a {@link TypeAdapter} or {@link TypeAdapterFactory}.

# File: `TypeAdapter.java`

## Method: `public final TypeAdapter<T> nullSafe()`

        <!-- META {"entityType": "Method", "entitySignature": "public final TypeAdapter<T> nullSafe()", "entityFile": "TypeAdapter.java"} -->This wrapper method is used to make a type adapter null tolerant. In general, a
        type adapter is required to handle nulls in write and read methods. Here is how this
        is typically done:<br>
        <pre>   {@code
        Gson gson = new GsonBuilder().registerTypeAdapter(Foo.class,
        new TypeAdapter<Foo>() {
        public Foo read(JsonReader in) throws IOException {
        if (in.peek() == JsonToken.NULL) {
        in.nextNull();
        return null;
        }
        // read a Foo from in and return it
        }
        public void write(JsonWriter out, Foo src) throws IOException {
        if (src == null) {
        out.nullValue();
        return;
        }
        // write src as JSON to out
        }
        }).create();
        }</pre>
        You can avoid this boilerplate handling of nulls by wrapping your type adapter with
        this method. Here is how we will rewrite the above example:
        <pre>   {@code
        Gson gson = new GsonBuilder().registerTypeAdapter(Foo.class,
        new TypeAdapter<Foo>() {
        public Foo read(JsonReader in) throws IOException {
        // read a Foo from in and return it
        }
        public void write(JsonWriter out, Foo src) throws IOException {
        // write src as JSON to out
        }
        }.nullSafe()).create();
        }</pre>
        Note that we didn't need to check for nulls in our type adapter after we used nullSafe.

# File: `$Gson$Types.java`

## Method: `public static WildcardType subtypeOf(Type bound)`

        <!-- META {"entityType": "Method", "entitySignature": "public static WildcardType subtypeOf(Type bound)", "entityFile": "$Gson$Types.java"} -->Returns a type that represents an unknown type that extends {@code bound}.
        For example, if {@code bound} is {@code CharSequence.class}, this returns
        {@code ? extends CharSequence}. If {@code bound} is {@code Object.class},
        this returns {@code ?}, which is shorthand for {@code ? extends Object}.

## Method: `public static WildcardType supertypeOf(Type bound)`

        <!-- META {"entityType": "Method", "entitySignature": "public static WildcardType supertypeOf(Type bound)", "entityFile": "$Gson$Types.java"} -->Returns a type that represents an unknown supertype of {@code bound}. For
        example, if {@code bound} is {@code String.class}, this returns {@code ?
        super String}.

# File: `None`

## None: `None`

        <!-- META {} -->This package provides annotations that can be used with {@link com.google.gson.Gson}.
        @author Inderjeet Singh, Joel Leitch
        */
        package com.google.gson.annotations;
        (package-info.java)
        This package provides annotations that can be used with {@link com.google.gson.Gson}.
        @author Inderjeet Singh, Joel Leitch

# File: `TypeAdapter.java`

## Method: `public final String toJson(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "public final String toJson(T value)", "entityFile": "TypeAdapter.java"} -->Converts {@code value} to a JSON document. Unlike Gson's similar {@link
        Gson#toJson(Object) toJson} method, this write is strict. Create a {@link
        JsonWriter#setLenient(boolean) lenient} {@code JsonWriter} and call
        {@link #write(com.google.gson.stream.JsonWriter, Object)} for lenient
        writing.
        @param value the Java object to convert. May be null.
        @since 2.2

# File: `$Gson$Types.java`

## Method: `public static Type canonicalize(Type type)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Type canonicalize(Type type)", "entityFile": "$Gson$Types.java"} -->Returns a type that is functionally equal but not necessarily equal
        according to {@link Object#equals(Object) Object.equals()}. The returned
        type is {@link java.io.Serializable}.

## Method: `public static boolean equals(Type a, Type b)`

        <!-- META {"entityType": "Method", "entitySignature": "public static boolean equals(Type a, Type b)", "entityFile": "$Gson$Types.java"} -->Returns true if {@code a} and {@code b} are equal.

## Method: `static Type getGenericSupertype(Type context, Class<?> rawType, Class<?> toResolve)`

        <!-- META {"entityType": "Method", "entitySignature": "static Type getGenericSupertype(Type context, Class<?> rawType, Class<?> toResolve)", "entityFile": "$Gson$Types.java"} -->Returns the generic supertype for {@code supertype}. For example, given a class {@code
        IntegerSet}, the result for when supertype is {@code Set.class} is {@code Set<Integer>} and the
        result when the supertype is {@code Collection.class} is {@code Collection<Integer>}.

## Method: `static Type getSupertype(Type context, Class<?> contextRawType, Class<?> supertype)`

        <!-- META {"entityType": "Method", "entitySignature": "static Type getSupertype(Type context, Class<?> contextRawType, Class<?> supertype)", "entityFile": "$Gson$Types.java"} -->Returns the generic form of {@code supertype}. For example, if this is {@code
        ArrayList<String>}, this returns {@code Iterable<String>} given the input {@code
        Iterable.class}.
        @param supertype a superclass of, or interface implemented by, this.

## Method: `public static Type getArrayComponentType(Type array)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Type getArrayComponentType(Type array)", "entityFile": "$Gson$Types.java"} -->Returns the component type of this array type.
        @throws ClassCastException if this type is not an array.

## Method: `public static Type getCollectionElementType(Type context, Class<?> contextRawType)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Type getCollectionElementType(Type context, Class<?> contextRawType)", "entityFile": "$Gson$Types.java"} -->Returns the element type of this collection type.
        @throws IllegalArgumentException if this type is not a collection.

## Method: `public static Type[] getMapKeyAndValueTypes(Type context, Class<?> contextRawType)`

        <!-- META {"entityType": "Method", "entitySignature": "public static Type[] getMapKeyAndValueTypes(Type context, Class<?> contextRawType)", "entityFile": "$Gson$Types.java"} -->Returns a two element array containing this map's key and value types in
        positions 0 and 1 respectively.

## Method: `private static Class<?> declaringClassOf(TypeVariable<?> typeVariable)`

        <!-- META {"entityType": "Method", "entitySignature": "private static Class<?> declaringClassOf(TypeVariable<?> typeVariable)", "entityFile": "$Gson$Types.java"} -->Returns the declaring class of {@code typeVariable}, or {@code null} if it was not declared by
        a class.

## Class: `WildcardTypeImpl`

        <!-- META {"entityType": "Class", "entitySignature": "WildcardTypeImpl", "entityFile": "$Gson$Types.java"} -->The WildcardType interface supports multiple upper bounds and multiple
        lower bounds. We only support what the Java 6 language needs - at most one
        bound. If a lower bound is set, the upper bound must be Object.class.

## Class: `$Gson$Types`

        <!-- META {"entityType": "Class", "entitySignature": "$Gson$Types", "entityFile": "$Gson$Types.java"} -->Static methods for working with types.
        @author Bob Lee
        @author Jesse Wilson

# File: `SerializedName.java`

## AnnotationMember: `value`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "value", "entityFile": "SerializedName.java"} -->@return the desired name of the field when it is serialized or deserialized

## AnnotationMember: `alternate`

        <!-- META {"entityType": "AnnotationMember", "entitySignature": "alternate", "entityFile": "SerializedName.java"} -->@return the alternative names of the field when it is deserialized

## Annotation: `SerializedName`

        <!-- META {"entityType": "Annotation", "entitySignature": "SerializedName", "entityFile": "SerializedName.java"} -->An annotation that indicates this member should be serialized to JSON with
        the provided name value as its field name.
        <p>This annotation will override any {@link com.google.gson.FieldNamingPolicy}, including
        the default field naming policy, that may have been set on the {@link com.google.gson.Gson}
        instance.  A different naming policy can set using the {@code GsonBuilder} class.  See
        {@link com.google.gson.GsonBuilder#setFieldNamingPolicy(com.google.gson.FieldNamingPolicy)}
        for more information.</p>
        <p>Here is an example of how this annotation is meant to be used:</p>
        <pre>
        public class MyClass {
        &#64SerializedName("name") String a;
        &#64SerializedName(value="name1", alternate={"name2", "name3"}) String b;
        String c;
        public MyClass(String a, String b, String c) {
        this.a = a;
        this.b = b;
        this.c = c;
        }
        }
        </pre>
        <p>The following shows the output that is generated when serializing an instance of the
        above example class:</p>
        <pre>
        MyClass target = new MyClass("v1", "v2", "v3");
        Gson gson = new Gson();
        String json = gson.toJson(target);
        System.out.println(json);
        ===== OUTPUT =====
        {"name":"v1","name1":"v2","c":"v3"}
        </pre>
        <p>NOTE: The value you specify in this annotation must be a valid JSON field name.</p>
        While deserializing, all values specified in the annotation will be deserialized into the field.
        For example:
        <pre>
        MyClass target = gson.fromJson("{'name1':'v1'}", MyClass.class);
        assertEquals("v1", target.b);
        target = gson.fromJson("{'name2':'v2'}", MyClass.class);
        assertEquals("v2", target.b);
        target = gson.fromJson("{'name3':'v3'}", MyClass.class);
        assertEquals("v3", target.b);
        </pre>
        Note that MyClass.b is now deserialized from either name1, name2 or name3.
        @see com.google.gson.FieldNamingPolicy
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TypeAdapter.java`

## Method: `public final JsonElement toJsonTree(T value)`

        <!-- META {"entityType": "Method", "entitySignature": "public final JsonElement toJsonTree(T value)", "entityFile": "TypeAdapter.java"} -->Converts {@code value} to a JSON tree.
        @param value the Java object to convert. May be null.
        @return the converted JSON tree. May be {@link JsonNull}.
        @since 2.2

## Method: `public abstract T read(JsonReader in) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract T read(JsonReader in) throws IOException", "entityFile": "TypeAdapter.java"} -->Reads one JSON value (an array, object, string, number, boolean or null)
        and converts it to a Java object. Returns the converted object.
        @return the converted Java object. May be null.

## Method: `public final T fromJson(Reader in) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public final T fromJson(Reader in) throws IOException", "entityFile": "TypeAdapter.java"} -->Converts the JSON document in {@code in} to a Java object. Unlike Gson's
        similar {@link Gson#fromJson(java.io.Reader, Class) fromJson} method, this
        read is strict. Create a {@link JsonReader#setLenient(boolean) lenient}
        {@code JsonReader} and call {@link #read(JsonReader)} for lenient reading.
        @return the converted Java object. May be null.
        @since 2.2

## Method: `public final T fromJson(String json) throws IOException`

        <!-- META {"entityType": "Method", "entitySignature": "public final T fromJson(String json) throws IOException", "entityFile": "TypeAdapter.java"} -->Converts the JSON document in {@code json} to a Java object. Unlike Gson's
        similar {@link Gson#fromJson(String, Class) fromJson} method, this read is
        strict. Create a {@link JsonReader#setLenient(boolean) lenient} {@code
        JsonReader} and call {@link #read(JsonReader)} for lenient reading.
        @return the converted Java object. May be null.
        @since 2.2

# File: `JsonSyntaxException.java`

## Method: `public JsonSyntaxException(Throwable cause)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonSyntaxException(Throwable cause)", "entityFile": "JsonSyntaxException.java"} -->Creates exception with the specified cause. Consider using
        {@link #JsonSyntaxException(String, Throwable)} instead if you can
        describe what actually happened.
        @param cause root exception that caused this exception to be thrown.

# File: `TypeAdapter.java`

## Method: `public final T fromJsonTree(JsonElement jsonTree)`

        <!-- META {"entityType": "Method", "entitySignature": "public final T fromJsonTree(JsonElement jsonTree)", "entityFile": "TypeAdapter.java"} -->Converts {@code jsonTree} to a Java object.
        @param jsonTree the Java object to convert. May be {@link JsonNull}.
        @since 2.2

# File: `JsonSyntaxException.java`

## Class: `JsonSyntaxException`

        <!-- META {"entityType": "Class", "entitySignature": "JsonSyntaxException", "entityFile": "JsonSyntaxException.java"} -->This exception is raised when Gson attempts to read (or write) a malformed
        JSON element.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `TypeAdapterFactory.java`

## Method: `TypeAdapter<T> create(Gson gson, TypeToken<T> type)`

        <!-- META {"entityType": "Method", "entitySignature": "TypeAdapter<T> create(Gson gson, TypeToken<T> type)", "entityFile": "TypeAdapterFactory.java"} -->Returns a type adapter for {@code type}, or null if this factory doesn't
        support {@code type}.

# File: `LongSerializationPolicy.java`

## EnumConstant: `DEFAULT`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "DEFAULT", "entityFile": "LongSerializationPolicy.java"} -->This is the "default" serialization policy that will output a {@code long} object as a JSON
        number.  For example, assume an object has a long field named "f" then the serialized output
        would be:
        {@code {"f":123}}.

# File: `TypeAdapterFactory.java`

## Interface: `TypeAdapterFactory`

        <!-- META {"entityType": "Interface", "entitySignature": "TypeAdapterFactory", "entityFile": "TypeAdapterFactory.java"} -->Creates type adapters for set of related types. Type adapter factories are
        most useful when several types share similar structure in their JSON form.
        <h3>Example: Converting enums to lowercase</h3>
        In this example, we implement a factory that creates type adapters for all
        enums. The type adapters will write enums in lowercase, despite the fact
        that they're defined in {@code CONSTANT_CASE} in the corresponding Java
        model: <pre>   {@code
        public class LowercaseEnumTypeAdapterFactory implements TypeAdapterFactory {
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
        Class<T> rawType = (Class<T>) type.getRawType();
        if (!rawType.isEnum()) {
        return null;
        }
        final Map<String, T> lowercaseToConstant = new HashMap<String, T>();
        for (T constant : rawType.getEnumConstants()) {
        lowercaseToConstant.put(toLowercase(constant), constant);
        }
        return new TypeAdapter<T>() {
        public void write(JsonWriter out, T value) throws IOException {
        if (value == null) {
        out.nullValue();
        } else {
        out.value(toLowercase(value));
        }
        }
        public T read(JsonReader reader) throws IOException {
        if (reader.peek() == JsonToken.NULL) {
        reader.nextNull();
        return null;
        } else {
        return lowercaseToConstant.get(reader.nextString());
        }
        }
        };
        }
        private String toLowercase(Object o) {
        return o.toString().toLowerCase(Locale.US);
        }
        }
        }</pre>
        <p>Type adapter factories select which types they provide type adapters
        for. If a factory cannot support a given type, it must return null when
        that type is passed to {@link #create}. Factories should expect {@code
        create()} to be called on them for many types and should return null for
        most of those types. In the above example the factory returns null for
        calls to {@code create()} where {@code type} is not an enum.
        <p>A factory is typically called once per type, but the returned type
        adapter may be used many times. It is most efficient to do expensive work
        like reflection in {@code create()} so that the type adapter's {@code
        read()} and {@code write()} methods can be very fast. In this example the
        mapping from lowercase name to enum value is computed eagerly.
        <p>As with type adapters, factories must be <i>registered</i> with a {@link
        com.google.gson.GsonBuilder} for them to take effect: <pre>   {@code
        GsonBuilder builder = new GsonBuilder();
        builder.registerTypeAdapterFactory(new LowercaseEnumTypeAdapterFactory());
        ...
        Gson gson = builder.create();
        }</pre>
        If multiple factories support the same type, the factory registered earlier
        takes precedence.
        <h3>Example: composing other type adapters</h3>
        In this example we implement a factory for Guava's {@code Multiset}
        collection type. The factory can be used to create type adapters for
        multisets of any element type: the type adapter for {@code
        Multiset<String>} is different from the type adapter for {@code
        Multiset<URL>}.
        <p>The type adapter <i>delegates</i> to another type adapter for the
        multiset elements. It figures out the element type by reflecting on the
        multiset's type token. A {@code Gson} is passed in to {@code create} for
        just this purpose: <pre>   {@code
        public class MultisetTypeAdapterFactory implements TypeAdapterFactory {
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
        Type type = typeToken.getType();
        if (typeToken.getRawType() != Multiset.class
        || !(type instanceof ParameterizedType)) {
        return null;
        }
        Type elementType = ((ParameterizedType) type).getActualTypeArguments()[0];
        TypeAdapter<?> elementAdapter = gson.getAdapter(TypeToken.get(elementType));
        return (TypeAdapter<T>) newMultisetAdapter(elementAdapter);
        }
        private <E> TypeAdapter<Multiset<E>> newMultisetAdapter(
        final TypeAdapter<E> elementAdapter) {
        return new TypeAdapter<Multiset<E>>() {
        public void write(JsonWriter out, Multiset<E> value) throws IOException {
        if (value == null) {
        out.nullValue();
        return;
        }
        out.beginArray();
        for (Multiset.Entry<E> entry : value.entrySet()) {
        out.value(entry.getCount());
        elementAdapter.write(out, entry.getElement());
        }
        out.endArray();
        }
        public Multiset<E> read(JsonReader in) throws IOException {
        if (in.peek() == JsonToken.NULL) {
        in.nextNull();
        return null;
        }
        Multiset<E> result = LinkedHashMultiset.create();
        in.beginArray();
        while (in.hasNext()) {
        int count = in.nextInt();
        E element = elementAdapter.read(in);
        result.add(element, count);
        }
        in.endArray();
        return result;
        }
        };
        }
        }
        }</pre>
        Delegating from one type adapter to another is extremely powerful; it's
        the foundation of how Gson converts Java objects and collections. Whenever
        possible your factory should retrieve its delegate type adapter in the
        {@code create()} method; this ensures potentially-expensive type adapter
        creation happens only once.
        @since 2.1

# File: `None`

## None: `None`

        <!-- META {} -->Copyright (C) 2008 Google Inc.
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.
        */
        package com.google.gson.internal;
        import java.io.Serializable;
        import java.lang.reflect.Array;
        import java.lang.reflect.GenericArrayType;
        import java.lang.reflect.GenericDeclaration;
        import java.lang.reflect.Modifier;
        import java.lang.reflect.ParameterizedType;
        import java.lang.reflect.Type;
        import java.lang.reflect.TypeVariable;
        import java.lang.reflect.WildcardType;
        import java.util.Arrays;
        import java.util.Collection;
        import java.util.Map;
        import java.util.NoSuchElementException;
        import java.util.Properties;
        import static com.google.gson.internal.$Gson$Preconditions.checkArgument;
        import static com.google.gson.internal.$Gson$Preconditions.checkNotNull;
        /**
        Static methods for working with types.
        @author Bob Lee
        @author Jesse Wilson
        */
        public final class $Gson$Types {
        static final Type[] EMPTY_TYPE_ARRAY = new Type[] {};
        private $Gson$Types() {
        throw new UnsupportedOperationException();
        }
        /**
        Returns a new parameterized type, applying {@code typeArguments} to
        {@code rawType} and enclosed by {@code ownerType}.
        @return a {@link java.io.Serializable serializable} parameterized type.
        */
        public static ParameterizedType newParameterizedTypeWithOwner(Type ownerType, Type rawType, Type... typeArguments) {
        return new ParameterizedTypeImpl(ownerType, rawType, typeArguments);
        }
        /**
        Returns an array type whose elements are all instances of
        {@code componentType}.
        @return a {@link java.io.Serializable serializable} generic array type.
        */
        public static GenericArrayType arrayOf(Type componentType) {
        return new GenericArrayTypeImpl(componentType);
        }
        /**
        Returns a type that represents an unknown type that extends {@code bound}.
        For example, if {@code bound} is {@code CharSequence.class}, this returns
        {@code ? extends CharSequence}. If {@code bound} is {@code Object.class},
        this returns {@code ?}, which is shorthand for {@code ? extends Object}.
        */
        public static WildcardType subtypeOf(Type bound) {
        return new WildcardTypeImpl(new Type[] { bound }, EMPTY_TYPE_ARRAY);
        }
        /**
        Returns a type that represents an unknown supertype of {@code bound}. For
        example, if {@code bound} is {@code String.class}, this returns {@code ?
        super String}.
        */
        public static WildcardType supertypeOf(Type bound) {
        return new WildcardTypeImpl(new Type[] { Object.class }, new Type[] { bound });
        }
        /**
        Returns a type that is functionally equal but not necessarily equal
        according to {@link Object#equals(Object) Object.equals()}. The returned
        type is {@link java.io.Serializable}.
        */
        public static Type canonicalize(Type type) {
        if (type instanceof Class) {
        Class<?> c = (Class<?>) type;
        return c.isArray() ? new GenericArrayTypeImpl(canonicalize(c.getComponentType())) : c;
        } else if (type instanceof ParameterizedType) {
        ParameterizedType p = (ParameterizedType) type;
        return new ParameterizedTypeImpl(p.getOwnerType(), p.getRawType(), p.getActualTypeArguments());
        } else if (type instanceof GenericArrayType) {
        GenericArrayType g = (GenericArrayType) type;
        return new GenericArrayTypeImpl(g.getGenericComponentType());
        } else if (type instanceof WildcardType) {
        WildcardType w = (WildcardType) type;
        return new WildcardTypeImpl(w.getUpperBounds(), w.getLowerBounds());
        } else {
        // type is either serializable as-is or unsupported
        return type;
        }
        }
        public static Class<?> getRawType(Type type) {
        if (type instanceof Class<?>) {
        // type is a normal class.
        return (Class<?>) type;
        } else if (type instanceof ParameterizedType) {
        ParameterizedType parameterizedType = (ParameterizedType) type;
        // I'm not exactly sure why getRawType() returns Type instead of Class.
        // Neal isn't either but suspects some pathological case related
        // to nested classes exists.
        Type rawType = parameterizedType.getRawType();
        checkArgument(rawType instanceof Class);
        return (Class<?>) rawType;
        } else if (type instanceof GenericArrayType) {
        Type componentType = ((GenericArrayType) type).getGenericComponentType();
        return Array.newInstance(getRawType(componentType), 0).getClass();
        } else if (type instanceof TypeVariable) {
        // having a raw type that's more general than necessary is okay
        return Object.class;
        } else if (type instanceof WildcardType) {
        return getRawType(((WildcardType) type).getUpperBounds()[0]);
        } else {
        String className = type == null ? "null" : type.getClass().getName();
        throw new IllegalArgumentException("Expected a Class, ParameterizedType, or " + "GenericArrayType, but <" + type + "> is of type " + className);
        }
        }
        static boolean equal(Object a, Object b) {
        return a == b || (a != null && a.equals(b));
        }
        /**
        Returns true if {@code a} and {@code b} are equal.
        */
        public static boolean equals(Type a, Type b) {
        if (a == b) {
        // also handles (a == null && b == null)
        return true;
        } else if (a instanceof Class) {
        // Class already specifies equals().
        return a.equals(b);
        } else if (a instanceof ParameterizedType) {
        if (!(b instanceof ParameterizedType)) {
        return false;
        }
        // TODO: save a .clone() call
        ParameterizedType pa = (ParameterizedType) a;
        ParameterizedType pb = (ParameterizedType) b;
        return equal(pa.getOwnerType(), pb.getOwnerType()) && pa.getRawType().equals(pb.getRawType()) && Arrays.equals(pa.getActualTypeArguments(), pb.getActualTypeArguments());
        } else if (a instanceof GenericArrayType) {
        if (!(b instanceof GenericArrayType)) {
        return false;
        }
        GenericArrayType ga = (GenericArrayType) a;
        GenericArrayType gb = (GenericArrayType) b;
        return equals(ga.getGenericComponentType(), gb.getGenericComponentType());
        } else if (a instanceof WildcardType) {
        if (!(b instanceof WildcardType)) {
        return false;
        }
        WildcardType wa = (WildcardType) a;
        WildcardType wb = (WildcardType) b;
        return Arrays.equals(wa.getUpperBounds(), wb.getUpperBounds()) && Arrays.equals(wa.getLowerBounds(), wb.getLowerBounds());
        } else if (a instanceof TypeVariable) {
        if (!(b instanceof TypeVariable)) {
        return false;
        }
        TypeVariable<?> va = (TypeVariable<?>) a;
        TypeVariable<?> vb = (TypeVariable<?>) b;
        return va.getGenericDeclaration() == vb.getGenericDeclaration() && va.getName().equals(vb.getName());
        } else {
        // This isn't a type we support. Could be a generic array type, wildcard type, etc.
        return false;
        }
        }
        static int hashCodeOrZero(Object o) {
        return o != null ? o.hashCode() : 0;
        }
        public static String typeToString(Type type) {
        return type instanceof Class ? ((Class<?>) type).getName() : type.toString();
        }
        /**
        Returns the generic supertype for {@code supertype}. For example, given a class {@code
        IntegerSet}, the result for when supertype is {@code Set.class} is {@code Set<Integer>} and the
        result when the supertype is {@code Collection.class} is {@code Collection<Integer>}.
        */
        static Type getGenericSupertype(Type context, Class<?> rawType, Class<?> toResolve) {
        if (toResolve == rawType) {
        return context;
        }
        // we skip searching through interfaces if unknown is an interface
        if (toResolve.isInterface()) {
        Class<?>[] interfaces = rawType.getInterfaces();
        for (int i = 0, length = interfaces.length; i < length; i++) {
        if (interfaces[i] == toResolve) {
        return rawType.getGenericInterfaces()[i];
        } else if (toResolve.isAssignableFrom(interfaces[i])) {
        return getGenericSupertype(rawType.getGenericInterfaces()[i], interfaces[i], toResolve);
        }
        }
        }
        // check our supertypes
        if (!rawType.isInterface()) {
        while (rawType != Object.class) {
        Class<?> rawSupertype = rawType.getSuperclass();
        if (rawSupertype == toResolve) {
        return rawType.getGenericSuperclass();
        } else if (toResolve.isAssignableFrom(rawSupertype)) {
        return getGenericSupertype(rawType.getGenericSuperclass(), rawSupertype, toResolve);
        }
        rawType = rawSupertype;
        }
        }
        // we can't resolve this further
        return toResolve;
        }
        /**
        Returns the generic form of {@code supertype}. For example, if this is {@code
        ArrayList<String>}, this returns {@code Iterable<String>} given the input {@code
        Iterable.class}.
        @param supertype a superclass of, or interface implemented by, this.
        */
        static Type getSupertype(Type context, Class<?> contextRawType, Class<?> supertype) {
        checkArgument(supertype.isAssignableFrom(contextRawType));
        return resolve(context, contextRawType, $Gson$Types.getGenericSupertype(context, contextRawType, supertype));
        }
        /**
        Returns the component type of this array type.
        @throws ClassCastException if this type is not an array.
        */
        public static Type getArrayComponentType(Type array) {
        return array instanceof GenericArrayType ? ((GenericArrayType) array).getGenericComponentType() : ((Class<?>) array).getComponentType();
        }
        /**
        Returns the element type of this collection type.
        @throws IllegalArgumentException if this type is not a collection.
        */
        public static Type getCollectionElementType(Type context, Class<?> contextRawType) {
        Type collectionType = getSupertype(context, contextRawType, Collection.class);
        if (collectionType instanceof WildcardType) {
        collectionType = ((WildcardType) collectionType).getUpperBounds()[0];
        }
        if (collectionType instanceof ParameterizedType) {
        return ((ParameterizedType) collectionType).getActualTypeArguments()[0];
        }
        return Object.class;
        }
        /**
        Returns a two element array containing this map's key and value types in
        positions 0 and 1 respectively.
        */
        public static Type[] getMapKeyAndValueTypes(Type context, Class<?> contextRawType) {
        /*
        Work around a problem with the declaration of java.util.Properties. That
        class should extend Hashtable<String, String>, but it's declared to
        extend Hashtable<Object, Object>.
        */
        if (context == Properties.class) {
        // TODO: test subclasses of Properties!
        return new Type[] { String.class, String.class };
        }
        Type mapType = getSupertype(context, contextRawType, Map.class);
        // TODO: strip wildcards?
        if (mapType instanceof ParameterizedType) {
        ParameterizedType mapParameterizedType = (ParameterizedType) mapType;
        return mapParameterizedType.getActualTypeArguments();
        }
        return new Type[] { Object.class, Object.class };
        }
        public static Type resolve(Type context, Class<?> contextRawType, Type toResolve) {
        // this implementation is made a little more complicated in an attempt to avoid object-creation
        while (true) {
        if (toResolve instanceof TypeVariable) {
        TypeVariable<?> typeVariable = (TypeVariable<?>) toResolve;
        toResolve = resolveTypeVariable(context, contextRawType, typeVariable);
        if (toResolve == typeVariable) {
        return toResolve;
        }
        } else if (toResolve instanceof Class && ((Class<?>) toResolve).isArray()) {
        Class<?> original = (Class<?>) toResolve;
        Type componentType = original.getComponentType();
        Type newComponentType = resolve(context, contextRawType, componentType);
        return componentType == newComponentType ? original : arrayOf(newComponentType);
        } else if (toResolve instanceof GenericArrayType) {
        GenericArrayType original = (GenericArrayType) toResolve;
        Type componentType = original.getGenericComponentType();
        Type newComponentType = resolve(context, contextRawType, componentType);
        return componentType == newComponentType ? original : arrayOf(newComponentType);
        } else if (toResolve instanceof ParameterizedType) {
        ParameterizedType original = (ParameterizedType) toResolve;
        Type ownerType = original.getOwnerType();
        Type newOwnerType = resolve(context, contextRawType, ownerType);
        boolean changed = newOwnerType != ownerType;
        Type[] args = original.getActualTypeArguments();
        for (int t = 0, length = args.length; t < length; t++) {
        Type resolvedTypeArgument = resolve(context, contextRawType, args[t]);
        if (resolvedTypeArgument != args[t]) {
        if (!changed) {
        args = args.clone();
        changed = true;
        }
        args[t] = resolvedTypeArgument;
        }
        }
        return changed ? newParameterizedTypeWithOwner(newOwnerType, original.getRawType(), args) : original;
        } else if (toResolve instanceof WildcardType) {
        WildcardType original = (WildcardType) toResolve;
        Type[] originalLowerBound = original.getLowerBounds();
        Type[] originalUpperBound = original.getUpperBounds();
        if (originalLowerBound.length == 1) {
        Type lowerBound = resolve(context, contextRawType, originalLowerBound[0]);
        if (lowerBound != originalLowerBound[0]) {
        return supertypeOf(lowerBound);
        }
        } else if (originalUpperBound.length == 1) {
        Type upperBound = resolve(context, contextRawType, originalUpperBound[0]);
        if (upperBound != originalUpperBound[0]) {
        return subtypeOf(upperBound);
        }
        }
        return original;
        } else {
        return toResolve;
        }
        }
        }
        static Type resolveTypeVariable(Type context, Class<?> contextRawType, TypeVariable<?> unknown) {
        Class<?> declaredByRaw = declaringClassOf(unknown);
        // we can't reduce this further
        if (declaredByRaw == null) {
        return unknown;
        }
        Type declaredBy = getGenericSupertype(context, contextRawType, declaredByRaw);
        if (declaredBy instanceof ParameterizedType) {
        int index = indexOf(declaredByRaw.getTypeParameters(), unknown);
        return ((ParameterizedType) declaredBy).getActualTypeArguments()[index];
        }
        return unknown;
        }
        private static int indexOf(Object[] array, Object toFind) {
        for (int i = 0; i < array.length; i++) {
        if (toFind.equals(array[i])) {
        return i;
        }
        }
        throw new NoSuchElementException();
        }
        /**
        Returns the declaring class of {@code typeVariable}, or {@code null} if it was not declared by
        a class.
        */
        private static Class<?> declaringClassOf(TypeVariable<?> typeVariable) {
        GenericDeclaration genericDeclaration = typeVariable.getGenericDeclaration();
        return genericDeclaration instanceof Class ? (Class<?>) genericDeclaration : null;
        }
        static void checkNotPrimitive(Type type) {
        checkArgument(!(type instanceof Class<?>) || !((Class<?>) type).isPrimitive());
        }
        private static final class ParameterizedTypeImpl implements ParameterizedType, Serializable {
        private final Type ownerType;
        private final Type rawType;
        private final Type[] typeArguments;
        public ParameterizedTypeImpl(Type ownerType, Type rawType, Type... typeArguments) {
        // require an owner type if the raw type needs it
        if (rawType instanceof Class<?>) {
        Class<?> rawTypeAsClass = (Class<?>) rawType;
        boolean isStaticOrTopLevelClass = Modifier.isStatic(rawTypeAsClass.getModifiers()) || rawTypeAsClass.getEnclosingClass() == null;
        checkArgument(ownerType != null || isStaticOrTopLevelClass);
        }
        this.ownerType = ownerType == null ? null : canonicalize(ownerType);
        this.rawType = canonicalize(rawType);
        this.typeArguments = typeArguments.clone();
        for (int t = 0; t < this.typeArguments.length; t++) {
        checkNotNull(this.typeArguments[t]);
        checkNotPrimitive(this.typeArguments[t]);
        this.typeArguments[t] = canonicalize(this.typeArguments[t]);
        }
        }
        public Type[] getActualTypeArguments() {
        return typeArguments.clone();
        }
        public Type getRawType() {
        return rawType;
        }
        public Type getOwnerType() {
        return ownerType;
        }
        @Override
        public boolean equals(Object other) {
        return other instanceof ParameterizedType && $Gson$Types.equals(this, (ParameterizedType) other);
        }
        @Override
        public int hashCode() {
        return Arrays.hashCode(typeArguments) ^ rawType.hashCode() ^ hashCodeOrZero(ownerType);
        }
        @Override
        public String toString() {
        StringBuilder stringBuilder = new StringBuilder(30 * (typeArguments.length + 1));
        stringBuilder.append(typeToString(rawType));
        if (typeArguments.length == 0) {
        return stringBuilder.toString();
        }
        stringBuilder.append("<").append(typeToString(typeArguments[0]));
        for (int i = 1; i < typeArguments.length; i++) {
        stringBuilder.append(", ").append(typeToString(typeArguments[i]));
        }
        return stringBuilder.append(">").toString();
        }
        private static final long serialVersionUID = 0;
        }
        private static final class GenericArrayTypeImpl implements GenericArrayType, Serializable {
        private final Type componentType;
        public GenericArrayTypeImpl(Type componentType) {
        this.componentType = canonicalize(componentType);
        }
        public Type getGenericComponentType() {
        return componentType;
        }
        @Override
        public boolean equals(Object o) {
        return o instanceof GenericArrayType && $Gson$Types.equals(this, (GenericArrayType) o);
        }
        @Override
        public int hashCode() {
        return componentType.hashCode();
        }
        @Override
        public String toString() {
        return typeToString(componentType) + "[]";
        }
        private static final long serialVersionUID = 0;
        }
        /**
        The WildcardType interface supports multiple upper bounds and multiple
        lower bounds. We only support what the Java 6 language needs - at most one
        bound. If a lower bound is set, the upper bound must be Object.class.
        */
        private static final class WildcardTypeImpl implements WildcardType, Serializable {
        private final Type upperBound;
        private final Type lowerBound;
        public WildcardTypeImpl(Type[] upperBounds, Type[] lowerBounds) {
        checkArgument(lowerBounds.length <= 1);
        checkArgument(upperBounds.length == 1);
        if (lowerBounds.length == 1) {
        checkNotNull(lowerBounds[0]);
        checkNotPrimitive(lowerBounds[0]);
        checkArgument(upperBounds[0] == Object.class);
        this.lowerBound = canonicalize(lowerBounds[0]);
        this.upperBound = Object.class;
        } else {
        checkNotNull(upperBounds[0]);
        checkNotPrimitive(upperBounds[0]);
        this.lowerBound = null;
        this.upperBound = canonicalize(upperBounds[0]);
        }
        }
        public Type[] getUpperBounds() {
        return new Type[] { upperBound };
        }
        public Type[] getLowerBounds() {
        return lowerBound != null ? new Type[] { lowerBound } : EMPTY_TYPE_ARRAY;
        }
        @Override
        public boolean equals(Object other) {
        return other instanceof WildcardType && $Gson$Types.equals(this, (WildcardType) other);
        }
        @Override
        public int hashCode() {
        // this equals Arrays.hashCode(getLowerBounds()) ^ Arrays.hashCode(getUpperBounds());
        return (lowerBound != null ? 31 + lowerBound.hashCode() : 1) ^ (31 + upperBound.hashCode());
        }
        @Override
        public String toString() {
        if (lowerBound != null) {
        return "? super " + typeToString(lowerBound);
        } else if (upperBound == Object.class) {
        return "?";
        } else {
        return "? extends " + typeToString(upperBound);
        }
        }
        private static final long serialVersionUID = 0;
        }
        }
        ($Gson$Types.java)
        Copyright (C) 2008 Google Inc.
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
        Unless required by applicable law or agreed to in writing, software
        distributed under the License is distributed on an "AS IS" BASIS,
        WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        See the License for the specific language governing permissions and
        limitations under the License.

# File: `LongSerializationPolicy.java`

## EnumConstant: `STRING`

        <!-- META {"entityType": "EnumConstant", "entitySignature": "STRING", "entityFile": "LongSerializationPolicy.java"} -->Serializes a long value as a quoted string.  For example, assume an object has a long field
        named "f" then the serialized output would be:
        {@code {"f":"123"}}.

## Method: `public abstract JsonElement serialize(Long value)`

        <!-- META {"entityType": "Method", "entitySignature": "public abstract JsonElement serialize(Long value)", "entityFile": "LongSerializationPolicy.java"} -->Serialize this {@code value} using this serialization policy.
        @param value the long value to be serialized into a {@link JsonElement}
        @return the serialized version of {@code value}

## Enum: `LongSerializationPolicy`

        <!-- META {"entityType": "Enum", "entitySignature": "LongSerializationPolicy", "entityFile": "LongSerializationPolicy.java"} -->Defines the expected format for a {@code long} or {@code Long} type when its serialized.
        @since 1.3
        @author Inderjeet Singh
        @author Joel Leitch

# File: `None`

## None: `None`

        <!-- META {} -->This package provides the {@link com.google.gson.Gson} class to convert Json to Java and
        vice-versa.
        <p>The primary class to use is {@link com.google.gson.Gson} which can be constructed with
        {@code new Gson()} (using default settings) or by using {@link com.google.gson.GsonBuilder}
        (to configure various options such as using versioning and so on).</p>
        @author Inderjeet Singh, Joel Leitch
        */
        package com.google.gson;
        (package-info.java)
        This package provides the {@link com.google.gson.Gson} class to convert Json to Java and
        vice-versa.
        <p>The primary class to use is {@link com.google.gson.Gson} which can be constructed with
        {@code new Gson()} (using default settings) or by using {@link com.google.gson.GsonBuilder}
        (to configure various options such as using versioning and so on).</p>
        @author Inderjeet Singh, Joel Leitch

## None: `None`

        <!-- META {} -->This package provides utility classes for finding type information for generic types.
        @author Inderjeet Singh, Joel Leitch
        */
        package com.google.gson.reflect;
        (package-info.java)
        This package provides utility classes for finding type information for generic types.
        @author Inderjeet Singh, Joel Leitch

# File: `JsonPrimitive.java`

## Method: `public JsonPrimitive(Boolean bool)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive(Boolean bool)", "entityFile": "JsonPrimitive.java"} -->Create a primitive containing a boolean value.
        @param bool the value to create the primitive with.

## Method: `public JsonPrimitive(Number number)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive(Number number)", "entityFile": "JsonPrimitive.java"} -->Create a primitive containing a {@link Number}.
        @param number the value to create the primitive with.

## Method: `public JsonPrimitive(String string)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive(String string)", "entityFile": "JsonPrimitive.java"} -->Create a primitive containing a String value.
        @param string the value to create the primitive with.

## Method: `public JsonPrimitive(Character c)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonPrimitive(Character c)", "entityFile": "JsonPrimitive.java"} -->Create a primitive containing a character. The character is turned into a one character String
        since Json only supports String.
        @param c the value to create the primitive with.

## Method: `JsonPrimitive(Object primitive)`

        <!-- META {"entityType": "Method", "entitySignature": "JsonPrimitive(Object primitive)", "entityFile": "JsonPrimitive.java"} -->Create a primitive using the specified Object. It must be an instance of {@link Number}, a
        Java primitive type, or a String.
        @param primitive the value to create the primitive with.

## Method: `public boolean isBoolean()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isBoolean()", "entityFile": "JsonPrimitive.java"} -->Check whether this primitive contains a boolean value.
        @return true if this primitive contains a boolean value, false otherwise.

## Method: `Boolean getAsBooleanWrapper()`

        <!-- META {"entityType": "Method", "entitySignature": "Boolean getAsBooleanWrapper()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link Boolean}.
        @return get this element as a {@link Boolean}.
        <!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public boolean getAsBoolean()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean getAsBoolean()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a boolean value.
        @return get this element as a primitive boolean value.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public boolean isNumber()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isNumber()", "entityFile": "JsonPrimitive.java"} -->Check whether this primitive contains a Number.
        @return true if this primitive contains a Number, false otherwise.

## Method: `public Number getAsNumber()`

        <!-- META {"entityType": "Method", "entitySignature": "public Number getAsNumber()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a Number.
        @return get this element as a Number.
        @throws NumberFormatException if the value contained is not a valid Number.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public boolean isString()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean isString()", "entityFile": "JsonPrimitive.java"} -->Check whether this primitive contains a String value.
        @return true if this primitive contains a String value, false otherwise.

## Method: `public String getAsString()`

        <!-- META {"entityType": "Method", "entitySignature": "public String getAsString()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a String.
        @return get this element as a String.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public double getAsDouble()`

        <!-- META {"entityType": "Method", "entitySignature": "public double getAsDouble()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive double.
        @return get this element as a primitive double.
        @throws NumberFormatException if the value contained is not a valid double.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public BigDecimal getAsBigDecimal()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigDecimal getAsBigDecimal()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link BigDecimal}.
        @return get this element as a {@link BigDecimal}.
        @throws NumberFormatException if the value contained is not a valid {@link BigDecimal}.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public BigInteger getAsBigInteger()`

        <!-- META {"entityType": "Method", "entitySignature": "public BigInteger getAsBigInteger()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a {@link BigInteger}.
        @return get this element as a {@link BigInteger}.
        @throws NumberFormatException if the value contained is not a valid {@link BigInteger}.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public float getAsFloat()`

        <!-- META {"entityType": "Method", "entitySignature": "public float getAsFloat()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a float.
        @return get this element as a float.
        @throws NumberFormatException if the value contained is not a valid float.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public long getAsLong()`

        <!-- META {"entityType": "Method", "entitySignature": "public long getAsLong()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive long.
        @return get this element as a primitive long.
        @throws NumberFormatException if the value contained is not a valid long.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public short getAsShort()`

        <!-- META {"entityType": "Method", "entitySignature": "public short getAsShort()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive short.
        @return get this element as a primitive short.
        @throws NumberFormatException if the value contained is not a valid short value.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `public int getAsInt()`

        <!-- META {"entityType": "Method", "entitySignature": "public int getAsInt()", "entityFile": "JsonPrimitive.java"} --><!-- 99ceab2c-1734-11ea-afaf-333445793454 <=< ACCEPT -->convenience method to get this element as a primitive integer.
        @return get this element as a primitive integer.
        @throws NumberFormatException if the value contained is not a valid integer.<!-- ACCEPT >=> 99ceab2c-1734-11ea-afaf-333445793454 -->

## Method: `private static boolean isIntegral(JsonPrimitive primitive)`

        <!-- META {"entityType": "Method", "entitySignature": "private static boolean isIntegral(JsonPrimitive primitive)", "entityFile": "JsonPrimitive.java"} -->Returns true if the specified number is an integral type
        (Long, Integer, Short, Byte, BigInteger)

## Class: `JsonPrimitive`

        <!-- META {"entityType": "Class", "entitySignature": "JsonPrimitive", "entityFile": "JsonPrimitive.java"} -->A class representing a Json primitive value. A primitive value
        is either a String, a Java primitive, or a Java primitive
        wrapper type.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `JsonSerializationContext.java`

## Method: `public JsonElement serialize(Object src)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement serialize(Object src)", "entityFile": "JsonSerializationContext.java"} -->Invokes default serialization on the specified object.
        @param src the object that needs to be serialized.
        @return a tree of {@link JsonElement}s corresponding to the serialized form of {@code src}.

## Method: `public JsonElement serialize(Object src, Type typeOfSrc)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement serialize(Object src, Type typeOfSrc)", "entityFile": "JsonSerializationContext.java"} -->Invokes default serialization on the specified object passing the specific type information.
        It should never be invoked on the element received as a parameter of the
        {@link JsonSerializer#serialize(Object, Type, JsonSerializationContext)} method. Doing
        so will result in an infinite loop since Gson will in-turn call the custom serializer again.
        @param src the object that needs to be serialized.
        @param typeOfSrc the actual genericized type of src object.
        @return a tree of {@link JsonElement}s corresponding to the serialized form of {@code src}.

## Interface: `JsonSerializationContext`

        <!-- META {"entityType": "Interface", "entitySignature": "JsonSerializationContext", "entityFile": "JsonSerializationContext.java"} -->Context for serialization that is passed to a custom serializer during invocation of its
        {@link JsonSerializer#serialize(Object, Type, JsonSerializationContext)} method.
        @author Inderjeet Singh
        @author Joel Leitch

# File: `JsonSerializer.java`

## Method: `public JsonElement serialize(T src, Type typeOfSrc, JsonSerializationContext context)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement serialize(T src, Type typeOfSrc, JsonSerializationContext context)", "entityFile": "JsonSerializer.java"} -->Gson invokes this call-back method during serialization when it encounters a field of the
        specified type.
        <p>In the implementation of this call-back method, you should consider invoking
        {@link JsonSerializationContext#serialize(Object, Type)} method to create JsonElements for any
        non-trivial field of the {@code src} object. However, you should never invoke it on the
        {@code src} object itself since that will cause an infinite loop (Gson will call your
        call-back method again).</p>
        @param src the object that needs to be converted to Json.
        @param typeOfSrc the actual type (fully genericized version) of the source object.
        @return a JsonElement corresponding to the specified object.

## Interface: `JsonSerializer`

        <!-- META {"entityType": "Interface", "entitySignature": "JsonSerializer", "entityFile": "JsonSerializer.java"} -->Interface representing a custom serializer for Json. You should write a custom serializer, if
        you are not happy with the default serialization done by Gson. You will also need to register
        this serializer through {@link com.google.gson.GsonBuilder#registerTypeAdapter(Type, Object)}.
        <p>Let us look at example where defining a serializer will be useful. The {@code Id} class
        defined below has two fields: {@code clazz} and {@code value}.</p>
        <p><pre>
        public class Id&lt;T&gt; {
        private final Class&lt;T&gt; clazz;
        private final long value;
        public Id(Class&lt;T&gt; clazz, long value) {
        this.clazz = clazz;
        this.value = value;
        }
        public long getValue() {
        return value;
        }
        }
        </pre></p>
        <p>The default serialization of {@code Id(com.foo.MyObject.class, 20L)} will be
        <code>{"clazz":com.foo.MyObject,"value":20}</code>. Suppose, you just want the output to be
        the value instead, which is {@code 20} in this case. You can achieve that by writing a custom
        serializer:</p>
        <p><pre>
        class IdSerializer implements JsonSerializer&lt;Id&gt;() {
        public JsonElement serialize(Id id, Type typeOfId, JsonSerializationContext context) {
        return new JsonPrimitive(id.getValue());
        }
        }
        </pre></p>
        <p>You will also need to register {@code IdSerializer} with Gson as follows:</p>
        <pre>
        Gson gson = new GsonBuilder().registerTypeAdapter(Id.class, new IdSerializer()).create();
        </pre>
        <p>New applications should prefer {@link TypeAdapter}, whose streaming API
        is more efficient than this interface's tree API.
        @author Inderjeet Singh
        @author Joel Leitch
        @param <T> type for which the serializer is being registered. It is possible that a serializer
        may be asked to serialize a specific generic type of the T.

# File: `JsonStreamParser.java`

## Method: `public JsonStreamParser(String json)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonStreamParser(String json)", "entityFile": "JsonStreamParser.java"} -->@param json The string containing JSON elements concatenated to each other.
        @since 1.4

## Method: `public JsonStreamParser(Reader reader)`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonStreamParser(Reader reader)", "entityFile": "JsonStreamParser.java"} -->@param reader The data stream containing JSON elements concatenated to each other.
        @since 1.4

## Method: `public JsonElement next() throws JsonParseException`

        <!-- META {"entityType": "Method", "entitySignature": "public JsonElement next() throws JsonParseException", "entityFile": "JsonStreamParser.java"} -->Returns the next available {@link JsonElement} on the reader. Null if none available.
        @return the next available {@link JsonElement} on the reader. Null if none available.
        @throws JsonParseException if the incoming stream is malformed JSON.
        @since 1.4

## Method: `public boolean hasNext()`

        <!-- META {"entityType": "Method", "entitySignature": "public boolean hasNext()", "entityFile": "JsonStreamParser.java"} -->Returns true if a {@link JsonElement} is available on the input for consumption
        @return true if a {@link JsonElement} is available on the input, false otherwise
        @since 1.4

## Method: `public void remove()`

        <!-- META {"entityType": "Method", "entitySignature": "public void remove()", "entityFile": "JsonStreamParser.java"} -->This optional {@link Iterator} method is not relevant for stream parsing and hence is not
        implemented.
        @since 1.4

## Class: `JsonStreamParser`

        <!-- META {"entityType": "Class", "entitySignature": "JsonStreamParser", "entityFile": "JsonStreamParser.java"} -->A streaming parser that allows reading of multiple {@link JsonElement}s from the specified reader
        asynchronously.
        <p>This class is conditionally thread-safe (see Item 70, Effective Java second edition). To
        properly use this class across multiple threads, you will need to add some external
        synchronization.  For example:
        <pre>
        JsonStreamParser parser = new JsonStreamParser("['first'] {'second':10} 'third'");
        JsonElement element;
        synchronized (parser) {  // synchronize on an object shared by threads
        if (parser.hasNext()) {
        element = parser.next();
        }
        }
        </pre>
        @author Inderjeet Singh
        @author Joel Leitch
        @since 1.4

